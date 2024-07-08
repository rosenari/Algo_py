"""
Z 패턴으로 재귀적으로 탐색하여 r 행 c 열을 몇번쨰로 방문하는지 체크
"""
import sys
import math


def Z(sR, sC, size, num):
    if size == 1:
        if sR == r and sC == c:
            print(num)
            exit(0)
        return

    new_size = size // 2

    if sR <= r < sR + new_size and sC <= c < sC + new_size:
        Z(sR, sC, new_size, num)
    if sR <= r < sR + new_size and sC + new_size <= c < sC + size:
        Z(sR, sC + new_size, new_size, num + (new_size ** 2) * 1)
    if sR + new_size <= r < sR + size and sC <= c < sC + new_size:
        Z(sR + new_size, sC, new_size, num + (new_size ** 2) * 2)
    if sR + new_size <= r < sR + size and sC + new_size <= c < sC + size:
        Z(sR + new_size, sC + new_size, new_size, num + (new_size ** 2) * 3)


input = sys.stdin.readline
N, r, c = map(int, input().split())
SIZE = int(math.pow(2, N))

Z(0, 0, SIZE, 0)
