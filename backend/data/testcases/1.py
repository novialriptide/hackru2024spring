import unittest
import argparse
import importlib.util


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_fizz_buzz(self):
        self.assertEqual(self.solution.fizzBuzz(3), ["1", "2", "Fizz"])
        self.assertEqual(self.solution.fizzBuzz(5), ["1", "2", "Fizz", "4", "Buzz"])
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

    unittest.main()
