import unittest


def solution(s):
    return int(s)


solution2 = int


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(1234, solution('1234'))
        self.assertEqual(-1234, solution('-1234'))
        self.assertEqual(1234, solution2('1234'))
        self.assertEqual(-1234, solution2('-1234'))


if __name__ == '__main__':
    unittest.main()
