import unittest

from day03.part02 import execute
from day03.util import parse_lines

test_file = "../data/task02_sample.txt"


class MyTestCase(unittest.TestCase):
    def test_parse_lines(self):
        lines = parse_lines(test_file)

        self.assertEqual(7, len(lines))  # add assertion here

    def test_execute(self):
        self.assertEqual(281, execute(test_file))


if __name__ == '__main__':
    unittest.main()
