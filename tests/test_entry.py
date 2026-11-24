import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import LINE


class TestOneLineLaugh(unittest.TestCase):
    def test_line_within_gate(self):
        self.assertGreaterEqual(len(LINE), 1)
        self.assertLessEqual(len(LINE), 200)

    def test_line_is_one_sentence(self):
        self.assertNotIn("\n", LINE)
        self.assertTrue(LINE.strip())
        self.assertEqual(LINE.count("."), 1)
        self.assertTrue(LINE.endswith("."))

    def test_line_is_not_whitespace_only(self):
        self.assertTrue(LINE.strip())

    def test_main_rejects_out_of_gate_line(self):
        import main as main_mod

        original = main_mod.LINE
        try:
            main_mod.LINE = "x" * 201
            with self.assertRaises(SystemExit):
                main_mod.main()
        finally:
            main_mod.LINE = original

    def test_writes_exact_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "entry.txt")
            subprocess.run(
                [sys.executable, "main.py", out],
                check=True,
                cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            )
            with open(out, "r", encoding="utf-8") as f:
                self.assertEqual(f.read(), LINE)


if __name__ == "__main__":
    unittest.main()
