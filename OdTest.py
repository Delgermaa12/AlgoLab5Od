from io import StringIO
import sys
import unittest
from Od import solve

class TestSolve(unittest.TestCase):
    def run_solve_with_input(self, input_str):
        original_stdin = sys.stdin
        original_stdout = sys.stdout
        sys.stdin = StringIO(input_str)
        sys.stdout = StringIO()
        try:
            solve()
            return sys.stdout.getvalue().strip()
        finally:
            sys.stdin = original_stdin
            sys.stdout = original_stdout

    def test_single_element(self):
        input_data = "1\n1\n42\n"
        expected_output = "0"
        result = self.run_solve_with_input(input_data)
        self.assertEqual(result, expected_output)
