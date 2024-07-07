import sys

"""
단지 번호 붙이기
단지를 이루는 (좌, 우, 상, 하 1로 연결된) 각 단지의 개수를 구하고 내림차수로 출력
"""

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(r, c):
    count = 1
    visited[r][c] = True

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N:
            if visited[nr][nc] is False and metrix[nr][nc] == 1:
                count += dfs(nr, nc)

    return count


input = sys.stdin.readline
N = int(input().rstrip())


metrix = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
answer = [dfs(i, j) for i in range(N) for j in range(N) if not visited[i][j] and metrix[i][j] != 0]

print(len(answer))
answer.sort()

for i in answer:
    print(i)