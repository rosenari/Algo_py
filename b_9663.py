import sys

"""
N x N 체스판 위에 N개의 퀸이 서로를 공격할수 없도록 배치할는 경우의 수
PyPy3로 해야 통과함. python3 로는 성능이...
"""


def dfs(row):
    result = 0

    if row == N:
        return 1

    for col in range(N):
        if is_possible(row, col):
            rows[row] = col
            result += dfs(row + 1)

    return result


def is_possible(row, col):
    for r in range(row):
        if rows[r] == col or abs(row - r) == abs(rows[r] - col):
            return False

    return True

N = int(sys.stdin.readline().rstrip())
rows = [-1] * N
print(dfs(0))