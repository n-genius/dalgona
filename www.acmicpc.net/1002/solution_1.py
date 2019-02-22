# https://www.acmicpc.net/problem/1002
from sys import stdin


def solution(x1, y1, r1, x2, y2, r2):
    distance = (x1-x2) ** 2 + (y1-y2) ** 2
    r1_plus_r2 = (r1+r2) ** 2
    r1_minus_r2 = (r1-r2) ** 2
    if x1 == x2 and y1 == y2 and r1 == r2:
        return -1
    elif distance > r1_plus_r2 or distance < r1_minus_r2:
        return 0
    elif distance == r1_plus_r2 or distance == r1_minus_r2:
        return 1
    return 2


if __name__ == '__main__':
    T = int(stdin.readline().rstrip())
    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, stdin.readline().rstrip().split())
        print(solution(x1, y1, r1, x2, y2, r2))

