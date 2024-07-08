import sys

"""
0은 하얀색
1은 파랑색
각 색상별 사각형의 개수를 구하시오.
"""


def recursive(sR, sC, dR, dC, N):
    if counting(sR, sC, dR, dC):
        return

    nN = N // 2
    recursive(sR, sC, dR - nN, dC - nN, nN)
    recursive(sR, sC + nN, dR - nN, dC, nN)
    recursive(sR + nN, sC, dR, dC - nN, nN)
    recursive(sR + nN, sC  + nN, dR, dC, nN)


def counting(sR, sC, dR, dC):
    sliced = [y for x in metrix[sR:dR + 1] for y in x[sC:dC + 1]]
    w = sliced.count(0)
    b = sliced.count(1)
    total = w + b


    if w == total:
        answer[0] += 1
    elif b == total:
        answer[1] += 1

    return w == total or b == total

# answer
answer = [0, 0]  # white, blue

NUM = int(sys.stdin.readline().rstrip())

metrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(NUM)]

recursive(0, 0, NUM - 1, NUM - 1, NUM)

print(answer[0])
print(answer[1])