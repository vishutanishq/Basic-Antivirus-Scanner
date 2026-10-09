import tempfile
import unittest
from pathlib import Path

from main import scan_file


class BasicScannerTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = Path(self.temp_dir.name) / "sample.txt"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_detects_demo_signature(self):
        self.file_path.write_bytes(b"example DEMO_MALWARE_MARKER content")
        self.assertTrue(scan_file(self.file_path))

    def test_clean_file_has_no_demo_signature(self):
        self.file_path.write_bytes(b"ordinary text")
        self.assertFalse(scan_file(self.file_path))

    def test_detects_second_demo_signature(self):
        self.file_path.write_bytes(b"ANTIVIRUS_DEMO_TEST_PATTERN")
        self.assertTrue(scan_file(self.file_path))


if __name__ == "__main__":
    unittest.main()
