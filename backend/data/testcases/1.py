import unittest
from snippets.question1 import Solution


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
    unittest.main()
