import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest

SCRIPT = Path(__file__).resolve().parent / 'contador.py'
spec = importlib.util.spec_from_file_location("exercise", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ExerciseTests(unittest.TestCase):

    def test_sequence(self): self.assertEqual(list(module.contar(3)),[1,2,3])
    def test_zero(self): self.assertEqual(list(module.contar(0)),[])
    def test_negative(self):
        with self.assertRaises(ValueError): module.contar(-1)

    def test_invalid_cli(self):
        result = subprocess.run([sys.executable, "-X", "utf8", str(SCRIPT)], input="invalid\n", text=True, capture_output=True, encoding="utf8", timeout=5)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Entrada inválida", result.stdout)
        self.assertNotIn("Traceback", result.stderr)

    def test_valid_cli(self):
        result = subprocess.run([sys.executable, "-X", "utf8", str(SCRIPT)], input='3\n', text=True, capture_output=True, encoding="utf8", timeout=5)
        self.assertEqual(result.returncode, 0)
        self.assertIn('1\n2\n3', result.stdout)


if __name__ == "__main__":
    unittest.main()
