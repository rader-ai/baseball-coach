#!/usr/bin/env python3
"""Independent arithmetic and input-boundary regressions; Python standard library."""

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "skills/baseball-coach/scripts/trace_opportunities.py"
SPEC = importlib.util.spec_from_file_location("opportunity_trace", HELPER)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
trace = MODULE.trace_opportunities


def visit(label="first", start=0, end=120, order=None, windows=None, cycle=30):
    return {"id": label, "start": start, "end": end,
            "windows": windows or [{"start": start, "end": end}],
            "cycle_seconds": cycle, "order": order or ["P1", "P2"]}


def by_player(model):
    return {p["label"]: p for p in trace(model)["players"]}


class OpportunityTraceTests(unittest.TestCase):
    def test_reported_twelve_player_failure(self):
        model = json.loads((ROOT / "evaluation/gap-regression/v3-model.json").read_text())
        results = by_player(model)
        self.assertEqual(len(results), 12)
        for group in "ABC":
            self.assertEqual([results[f"{group}{n}"]["attempts"] for n in range(1, 5)],
                             [7, 8, 8, 7])
            gaps = [next(g for g in results[f"{group}{n}"]["gaps"]
                         if g["kind"] == "between_visits") for n in range(1, 5)]
            expected = [1605, 1465, 1465, 1605] if group == "B" else [645, 505, 505, 645]
            self.assertEqual([g["start_to_start_seconds"] for g in gaps], expected)
            self.assertEqual([g["end_to_start_seconds"] for g in gaps], [n - 35 for n in expected])
        # Independently enumerated child turn starts include setup and both full rotations.
        self.assertEqual([e["start"] for e in results["B1"]["events"]],
                         [420, 560, 700, 840, 2445, 2585, 2725])
        self.assertEqual([e["start"] for e in results["C4"]["events"]],
                         [525, 665, 805, 1450, 1590, 1730, 1870])
        within = [g["start_to_start_seconds"] for p in results.values()
                  for g in p["gaps"] if g["kind"] == "within_visit"]
        self.assertEqual(set(within), {140})

    def test_pauses_keep_order_and_discard_short_tails(self):
        results = by_player({"players": ["A", "B", "C", "D"], "visits": [visit(
            end=300, order=["A", "B", "C"],
            windows=[{"start": 30, "end": 95}, {"start": 150, "end": 215}])]})
        self.assertEqual([e["start"] for e in results["A"]["events"]], [30, 180])
        self.assertEqual([e["start"] for e in results["B"]["events"]], [60])
        self.assertEqual([e["start"] for e in results["C"]["events"]], [150])
        self.assertEqual([e["window_index"] for e in results["A"]["events"]], [0, 1])
        gap = results["A"]["gaps"][0]
        self.assertEqual((gap["kind"], gap["start_to_start_seconds"], gap["end_to_start_seconds"]),
                         ("within_visit", 150, 120))
        self.assertEqual(results["D"], {"label": "D", "attempts": 0, "events": [], "gaps": []})

    def test_complete_cycle_boundary_and_empty_results(self):
        for end, expected in [(29, 0), (30, 1), (59, 1), (60, 2)]:
            with self.subTest(end=end):
                p = by_player({"players": ["P1"], "visits": [visit(end=end, order=["P1"])]})["P1"]
                self.assertEqual(p["attempts"], expected)
                self.assertTrue(all(e["end"] <= end for e in p["events"]))
        empty = by_player({"players": ["P1"], "visits": []})["P1"]
        self.assertEqual((empty["attempts"], empty["gaps"]), (0, []))

    def test_one_lane_fallback_has_no_cross_visit_gap(self):
        model = json.loads((ROOT / "evaluation/gap-regression/v3-model.json").read_text())
        # One fielding visit per group in chronological, nonconcurrent lane slots.
        model["visits"] = [v for v in model["visits"] if v["id"] in {"C-1", "A-1", "B-2"}]
        results = by_player(model)
        for group in "ABC":
            self.assertEqual(sorted(results[f"{group}{n}"]["attempts"] for n in range(1, 5)), [3, 4, 4, 4])
        self.assertFalse(any(g["kind"] == "between_visits" for p in results.values() for g in p["gaps"]))

    def test_overlap_depends_on_declared_child_not_lane(self):
        disjoint = {"players": ["P1", "P2"], "visits": [
            visit("a", order=["P1"]), visit("b", order=["P2"])]}
        self.assertEqual(sum(p["attempts"] for p in trace(disjoint)["players"]), 8)
        overlap = copy.deepcopy(disjoint)
        overlap["visits"][1]["order"] = ["P1"]
        overlap["visits"][0]["windows"] = [{"start": 0, "end": 30}]
        overlap["visits"][1]["windows"] = [{"start": 60, "end": 90}]
        with self.assertRaisesRegex(ValueError, "overlapping visits"):
            trace(overlap)
        # Adjacent visits are valid; input order need not be chronological.
        adjacent = {"players": ["P1"], "visits": [
            visit("later", 120, 150, ["P1"]), visit("earlier", 0, 30, ["P1"])]}
        self.assertEqual([e["start"] for e in by_player(adjacent)["P1"]["events"]], [0, 120])

    def test_malformed_models_are_rejected(self):
        base = {"players": ["P1", "P2"], "visits": [visit()]}
        invalid = []
        for key, values in {
            "cycle_seconds": [0, -1, True, 1.5, "30"],
            "start": [-1, True, 0.5, "0", 120],
            "end": [0, -1, False, 120.5],
            "order": [[], ["P1", "P1"], ["unknown"], "P1"],
            "windows": [[], [{"start": 0, "end": 121}], [{"start": 20, "end": 20}],
                        [{"start": 0, "end": 60}, {"start": 30, "end": 90}],
                        [{"start": 60, "end": 90}, {"start": 0, "end": 30}],
                        [{"start": True, "end": 30}], [{"start": 0, "end": 30, "extra": 1}]],
        }.items():
            for value in values:
                data = copy.deepcopy(base)
                data["visits"][0][key] = value
                invalid.append((f"visit {key}={value!r}", data))
        for players in [[], ["P1", "P1"], [" P1"], [""], [1], "P1"]:
            data = copy.deepcopy(base)
            data["players"] = players
            invalid.append((f"players={players!r}", data))
        duplicate = copy.deepcopy(base)
        duplicate["visits"].append(copy.deepcopy(duplicate["visits"][0]))
        invalid.extend([("duplicate visit id", duplicate), ("unknown key", {**base, "extra": 1}),
                        ("missing key", {"players": ["P1"]}), ("wrong type", []),
                        ("visits wrong type", {"players": ["P1"], "visits": {}})])
        for label, data in invalid:
            with self.subTest(label=label), self.assertRaises(ValueError):
                trace(data)

    def test_cli_file_stdin_parity_and_clear_failures(self):
        model = {"players": ["P1", "P2"], "visits": [visit()]}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "model.json"
            path.write_text(json.dumps(model))
            file_run = subprocess.run([sys.executable, str(HELPER), str(path)], capture_output=True, text=True)
            stdin_run = subprocess.run([sys.executable, str(HELPER), "-"], input=json.dumps(model),
                                       capture_output=True, text=True)
        self.assertEqual((file_run.returncode, stdin_run.returncode), (0, 0))
        self.assertEqual(json.loads(file_run.stdout), trace(model))
        self.assertEqual(file_run.stdout, stdin_run.stdout)
        for bad in ["{", '{"players":["P1"],"players":["P2"],"visits":[]}',
                    '{"players":["P1"],"visits":null}']:
            result = subprocess.run([sys.executable, str(HELPER), "-"], input=bad, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(result.stdout, "")
            self.assertIn("Invalid opportunity model:", result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
