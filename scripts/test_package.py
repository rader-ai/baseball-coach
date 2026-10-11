#!/usr/bin/env python3
"""Exercise distribution boundaries without network or production operations."""
from pathlib import Path
import tempfile
import unittest
import zipfile
from check_package import release_files, make_archive


class PackageBoundaries(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        (self.root / 'approved.md').write_text('Fictional review example.\n')
        (self.root / 'private-roster.csv').write_text('Synthetic test canary only.\n')
        (self.root / 'release-files.txt').write_text('approved.md\n')

    def test_archive_excludes_unlisted_files_and_is_repeatable(self):
        files = release_files(self.root)
        one, two = self.root / 'one.zip', self.root / 'two.zip'
        self.assertEqual(make_archive(self.root, files, one), make_archive(self.root, files, two))
        with zipfile.ZipFile(one) as archive:
            self.assertEqual(archive.namelist(), ['baseball-coach/approved.md'])
        with self.assertRaises(FileExistsError):
            make_archive(self.root, files, one)

    def test_rejects_traversal_and_hidden_paths(self):
        for name in ('../secret.md', '/tmp/secret.md', '.git/config', './approved.md', 'a\\secret.md'):
            (self.root / 'release-files.txt').write_text(name + '\n')
            with self.subTest(name=name), self.assertRaises(ValueError):
                release_files(self.root)

    def test_rejects_symlink_even_to_allowed_file(self):
        (self.root / 'linked.md').symlink_to(self.root / 'approved.md')
        (self.root / 'release-files.txt').write_text('linked.md\n')
        with self.assertRaises(ValueError):
            release_files(self.root)

    def test_rejects_duplicate_or_missing_inventory_items(self):
        for value in ('approved.md\napproved.md\n', 'missing.md\n'):
            (self.root / 'release-files.txt').write_text(value)
            with self.subTest(value=value), self.assertRaises(ValueError):
                release_files(self.root)


if __name__ == '__main__':
    unittest.main()
