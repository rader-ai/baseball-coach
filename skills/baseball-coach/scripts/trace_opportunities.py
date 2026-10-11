#!/usr/bin/env python3
"""Trace an explicit turn model; no coaching, safety, or success verdict.

Usage: python3 trace_opportunities.py model.json   (or '-' for stdin)
All times are nonnegative integer elapsed seconds. Input:
{"players": ["P1", "P2"], "visits": [
  {"id": "first", "start": 0, "end": 120,
   "windows": [{"start": 10, "end": 110}],
   "cycle_seconds": 30, "order": ["P1", "P2"]}
]}
Windows must be explicit, ordered, nonoverlapping, and inside their visit.
Only complete cycles fit. Round-robin order continues across windows of one
visit, then resets to the explicit order of the next visit. Window indices
are zero-based. Visit order declares participants, even if they get no turn.
Omitted time is not classified or inferred. Gaps are between consecutive
modeled attempts at the ONE target activity represented by this input.
"""

import argparse
import json
import sys


def _object(value, keys, where):
    if not isinstance(value, dict) or set(value) != set(keys):
        raise ValueError(f"{where}: expected exactly these keys: {', '.join(keys)}")


def _label(value, where):
    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{where}: expected a nonempty label without edge whitespace")
    return value


def _seconds(value, where, positive=False):
    if type(value) is not int or value < (1 if positive else 0):
        kind = "positive" if positive else "nonnegative"
        raise ValueError(f"{where}: expected {kind} integer seconds")
    return value


def _labels(value, where):
    if not isinstance(value, list) or not value:
        raise ValueError(f"{where}: expected a nonempty list of labels")
    labels = [_label(item, f"{where}[{i}]") for i, item in enumerate(value)]
    if len(set(labels)) != len(labels):
        raise ValueError(f"{where}: duplicate labels")
    return labels


def _validate(data):
    _object(data, ("players", "visits"), "model")
    players = _labels(data["players"], "players")
    known = set(players)
    if not isinstance(data["visits"], list):
        raise ValueError("visits: expected a list")
    visits, ids = [], set()
    assignments = {player: [] for player in players}
    for index, item in enumerate(data["visits"]):
        where = f"visits[{index}]"
        _object(item, ("id", "start", "end", "windows", "cycle_seconds", "order"), where)
        visit_id = _label(item["id"], f"{where}.id")
        if visit_id in ids:
            raise ValueError(f"{where}.id: duplicate visit id {visit_id!r}")
        ids.add(visit_id)
        start = _seconds(item["start"], f"{where}.start")
        end = _seconds(item["end"], f"{where}.end")
        if end <= start:
            raise ValueError(f"{where}: end must be later than start")
        cycle = _seconds(item["cycle_seconds"], f"{where}.cycle_seconds", positive=True)
        order = _labels(item["order"], f"{where}.order")
        if not set(order) <= known:
            raise ValueError(f"{where}.order: contains undeclared player labels")
        if not isinstance(item["windows"], list) or not item["windows"]:
            raise ValueError(f"{where}.windows: expected a nonempty list")
        windows, prior_end = [], start
        for j, window in enumerate(item["windows"]):
            position = f"{where}.windows[{j}]"
            _object(window, ("start", "end"), position)
            ws = _seconds(window["start"], f"{position}.start")
            we = _seconds(window["end"], f"{position}.end")
            if not start <= ws < we <= end:
                raise ValueError(f"{position}: window must be positive and inside its visit")
            if ws < prior_end:
                raise ValueError(f"{position}: windows must be ordered and nonoverlapping")
            windows.append({"start": ws, "end": we})
            prior_end = we
        visits.append({"id": visit_id, "start": start, "end": end,
                       "windows": windows, "cycle_seconds": cycle, "order": order})
        for player in order:
            assignments[player].append((start, end, visit_id))

    for player, intervals in assignments.items():
        intervals.sort()
        for previous, following in zip(intervals, intervals[1:]):
            if following[0] < previous[1]:
                raise ValueError(
                    f"player {player!r}: overlapping visits {previous[2]!r} and {following[2]!r}"
                )
    return players, visits


def trace_opportunities(data):
    """Return validated model and per-player events/gaps; raise ValueError on invalid input."""
    players, visits = _validate(data)
    timelines = {player: [] for player in players}
    for visit in visits:
        next_index = 0
        cycle = visit["cycle_seconds"]
        for window_index, window in enumerate(visit["windows"]):
            # Unused tails are discarded, never combined across a window break.
            for start in range(window["start"], window["end"] - cycle + 1, cycle):
                player = visit["order"][next_index % len(visit["order"])]
                timelines[player].append({"visit": visit["id"], "window_index": window_index,
                                          "start": start, "end": start + cycle})
                next_index += 1

    results = []
    for player in players:
        events = sorted(timelines[player], key=lambda event: event["start"])
        gaps = []
        for previous, following in zip(events, events[1:]):
            gaps.append({
                "kind": "within_visit" if previous["visit"] == following["visit"] else "between_visits",
                "previous": previous.copy(), "next": following.copy(),
                "start_to_start_seconds": following["start"] - previous["start"],
                "end_to_start_seconds": following["start"] - previous["end"],
            })
        results.append({"label": player, "attempts": len(events), "events": events, "gaps": gaps})
    return {
        "model": {
            "time_unit": "elapsed_seconds", "players": players, "visits": visits,
            "window_index_base": 0,
            "cycle_policy": "complete_cycles_only",
            "window_order_policy": "continue_round_robin_within_visit",
            "visit_order_policy": "reset_to_each_explicit_order",
            "limitations": [
                "One explicitly modeled target activity; synthetic labels only.",
                "Modeled attempts are not successes, observed rates, or promised opportunities.",
                "Gaps include all elapsed time; end-to-start is not necessarily idle waiting.",
                "No overhead is inferred; omitted time and other activities are not classified.",
                "No safety, feasibility, adequacy, or global gap-bound verdict is provided.",
            ],
        },
        "players": results,
    }


def _unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key!r}")
        result[key] = value
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", help="JSON model path, or '-' to read stdin")
    args = parser.parse_args(argv)
    try:
        if args.input == "-":
            data = json.load(sys.stdin, object_pairs_hook=_unique_keys)
        else:
            with open(args.input, encoding="utf-8") as source:
                data = json.load(source, object_pairs_hook=_unique_keys)
        result = trace_opportunities(data)
    except (ValueError, OSError, UnicodeError) as error:
        print(f"Invalid opportunity model: {error}", file=sys.stderr)
        return 2
    json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
