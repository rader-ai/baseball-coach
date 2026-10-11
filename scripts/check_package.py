#!/usr/bin/env python3
"""Check and archive only explicitly approved text files; Python standard library.

The metadata check intentionally supports this package's flat scalar YAML only.
This is not a general YAML/schema validator or proof of privacy/coaching safety.
"""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def release_files(root):
    names = [line.strip() for line in (root / 'release-files.txt').read_text().splitlines()
             if line.strip() and not line.startswith('#')]
    if not names or len(names) != len(set(names)):
        raise ValueError('Release inventory must be nonempty and have no duplicates')
    paths = []
    for name in names:
        relative = PurePosixPath(name)
        if (name != relative.as_posix() or '\\' in name or relative.is_absolute()
                or any(p in {'..', '.'} or p.startswith('.') for p in relative.parts)):
            raise ValueError(f'Unsafe release path: {name}')
        path = root / name
        if any(p.is_symlink() for p in [path, *path.parents] if p != root.parent):
            raise ValueError(f'Symlink in release path: {name}')
        if not path.is_file() or not path.resolve().is_relative_to(root.resolve()):
            raise ValueError(f'Missing or escaping release file: {name}')
        if path.suffix not in {'.md', '.yaml', '.json', '.py', '.txt'} or path.stat().st_size > 256 * 1024:
            raise ValueError(f'Unexpected type or oversized release file: {name}')
        path.read_text(encoding='utf-8')
        paths.append(path)
    return sorted(paths)


def check_metadata(root):
    skill = root / 'skills/baseball-coach/SKILL.md'
    text = skill.read_text()
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    if not match:
        raise ValueError('Missing SKILL.md YAML frontmatter')
    fields = {}
    for line in match[1].splitlines():
        key, separator, value = line.partition(':')
        if not separator or key in fields:
            raise ValueError('Expected unique flat scalar metadata fields')
        value = value.strip()
        if value.startswith('"'):
            value = json.loads(value)
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        fields[key] = value
    if set(fields) != {'name', 'description'}:
        raise ValueError('This draft expects only name and description metadata')
    if fields['name'] != skill.parent.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', fields['name']):
        raise ValueError('Skill name must match its folder and use lowercase hyphens')
    if not 1 <= len(fields['name']) <= 64 or not 1 <= len(fields['description']) <= 1024:
        raise ValueError('Skill metadata length outside Agent Skills constraints')
    if len(text.splitlines()) >= 500:
        raise ValueError('Entrypoint should remain below 500 lines')
    manifest = json.loads((root / 'plugin.json').read_text())
    expected = {'$schema', 'name', 'version', 'description'}
    if set(manifest) != expected or manifest['name'] != fields['name']:
        raise ValueError('Unexpected minimal plugin manifest fields or identity')
    if manifest['$schema'] != 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json':
        raise ValueError('Unexpected plugin schema URL')
    if not re.fullmatch(r'\d+\.\d+\.\d+', manifest['version']):
        raise ValueError('Expected numeric semantic version')
    return len(text.splitlines())


def check_links(root, paths):
    count = 0
    released = set(paths)
    for path in paths:
        if path.suffix != '.md':
            continue
        text = path.read_text()
        if re.search(r'(?:/Users/|/home/|file://|BEGIN (?:RSA |OPENSSH )?PRIVATE KEY)', text):
            raise ValueError(f'Host path or key marker in distribution: {path.name}')
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
            target = target.strip('<>')
            if target.startswith(('https://', 'http://', '#')):
                continue
            target = target.split('#', 1)[0]
            linked = (path.parent / target).resolve()
            if not linked.is_relative_to(root.resolve()) or not linked.exists():
                raise ValueError(f'Broken/escaping link in {path.name}: {target}')
            if linked.is_file() and linked not in released:
                raise ValueError(f'Link to unpackaged file in {path.name}: {target}')
            if path.is_relative_to(root / 'skills') and not linked.is_relative_to(root / 'skills/baseball-coach'):
                raise ValueError(f'Skill link depends on outer repository: {target}')
            count += 1
    return count


def check_sample_times(root):
    checked = 0
    for path in sorted((root / 'skills/baseball-coach/examples').glob('*.md')):
        text = path.read_text()
        total = re.search(r'Total: (\d+) minutes', text)
        if not total:
            continue
        spans = [tuple(map(int, m)) for m in re.findall(r'^\| (\d+)–(\d+) \|', text, re.M)]
        if (not spans or spans[0][0] != 0 or any(end <= start for start, end in spans)
                or any(start != prev[1] for prev, (start, end) in zip(spans, spans[1:]))
                or spans[-1][1] != int(total.group(1))):
            raise ValueError(f'Sample timing gap/overlap/total mismatch: {path.name}')
        checked += 1
    if checked != 4:
        raise ValueError('Expected four timed sample plans in this edition')
    return checked


def make_archive(root, paths, destination):
    destination = destination.resolve()
    if destination in paths:
        raise ValueError('Archive cannot overwrite an input')
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation prevents silently replacing an earlier review artifact.
    with zipfile.ZipFile(destination, 'x', compression=zipfile.ZIP_DEFLATED) as archive:
        for path in paths:
            name = 'baseball-coach/' + path.relative_to(root).as_posix()
            info = zipfile.ZipInfo(name, date_time=(2026, 10, 11, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    with zipfile.ZipFile(destination) as archive:
        expected = ['baseball-coach/' + p.relative_to(root).as_posix() for p in paths]
        if archive.namelist() != expected or archive.testzip() is not None:
            raise ValueError('Archive membership or CRC verification failed')
    return hashlib.sha256(destination.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archive', type=Path)
    args = parser.parse_args()
    paths = release_files(ROOT)
    lines = check_metadata(ROOT)
    links = check_links(ROOT, paths)
    clocks = check_sample_times(ROOT)
    print(f'PASS: {len(paths)} allowlisted text files, {links} local links, {clocks} sample clocks, SKILL.md {lines} lines')
    if args.archive:
        digest = make_archive(ROOT, paths, args.archive)
        print(f'ARCHIVE: {args.archive}\nSHA256: {digest}')
    print('Manual coaching/privacy review and host testing remain separate.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        sys.exit(1)
