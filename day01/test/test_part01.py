import unittest

from day01.part01 import execute
from day01.util import parse_lines


test_file = "data/task01_sample.txt"


class MyTestCase(unittest.TestCase):
    def test_parse_lines(self):
        lines = parse_lines(test_file)

        self.assertEqual(4, len(lines))  # add assertion here

    def test_execute(self):
        self.assertEqual(142, execute(test_file))


if __name__ == '__main__':
    unittest.main()
