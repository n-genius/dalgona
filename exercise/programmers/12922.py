import unittest


def solution(n):
    return '수박' * (n // 2) + '수' * (n % 2)


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        self.assertEqual('수박수', solution(3))
        self.assertEqual('수박수박', solution(4))


if __name__ == '__main__':
    unittest.main()
