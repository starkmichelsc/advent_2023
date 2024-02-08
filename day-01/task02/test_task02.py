import unittest

from task02 import execute, parse_lines

class MyTestCase(unittest.TestCase):
    def test_parse_lines(self):
        lines = parse_lines("task02_sample.txt")

        self.assertEqual(7, len(lines))  # add assertion here

    def test_execute(self):
        self.assertEqual(281, execute("task02_sample.txt"))


if __name__ == '__main__':
    unittest.main()
