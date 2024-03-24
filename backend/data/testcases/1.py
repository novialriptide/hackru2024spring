import unittest
import sys
import argparse
import importlib.util


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_fizz_buzz_3(self):
        self.assertEqual(self.solution.fizzBuzz(3), ["1", "2", "Fizz"])

    def test_fizz_buzz_5(self):
        self.assertEqual(self.solution.fizzBuzz(5), ["1", "2", "Fizz", "4", "Buzz"])

    def test_fizz_buzz_15(self):
        self.assertEqual(
            self.solution.fizzBuzz(15),
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ],
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "solution_file", help="The Python file containing the Solution class"
    )
    args = parser.parse_args()

    spec = importlib.util.spec_from_file_location("solution", args.solution_file)
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    Solution = solution_module.Solution

    suite = unittest.defaultTestLoader.loadTestsFromTestCase(MyTestCase)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    total_cases = result.testsRun
    failed_cases = len(result.failures) + len(result.errors)
    passed_cases = total_cases - failed_cases

    print(f"{passed_cases}/{total_cases}")
