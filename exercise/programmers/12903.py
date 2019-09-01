import unittest


def solution(s):
    return s[(len(s) - 1) // 2:len(s) // 2 + 1]


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual('w', solution('power'))
        self.assertEqual('es', solution('test'))


if __name__ == '__main__':
    unittest.main()

