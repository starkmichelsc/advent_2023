import unittest

from day02.part01 import execute
from day02.util import parse_lines


test_file = "../data/task01_sample.txt"


class MyTestCase(unittest.TestCase):
    def test_parse_lines(self):
        lines = parse_lines(test_file)

        self.assertEqual(5, len(lines))  # add assertion here

    def test_execute(self):
        self.assertEqual(8, execute(test_file))

if __name__ == '__main__':
    unittest.main()
