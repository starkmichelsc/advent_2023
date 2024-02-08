import unittest

from task01 import execute, parse_lines


class MyTestCase(unittest.TestCase):
    def test_parse_lines(self):
        lines = parse_lines("task01_sample.txt")

        self.assertEqual(4, len(lines))  # add assertion here

    def test_execute(self):
        self.assertEqual(142, execute("task01_sample.txt"))


if __name__ == '__main__':
    unittest.main()
