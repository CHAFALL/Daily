from collections import deque

def bfs():
    Q = deque()
    Q.append((0, 0))
    visited[0][0] = 1

    while Q:
        i, j = Q.popleft()
        # 종료 조건
        if i == N - 1 and j == M - 1:
            return visited[N - 1][M - 1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
                if not visited[ni][nj]:
                    visited[ni][nj] = visited[i][j] + 1
                    Q.append((ni, nj))


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

visited = [[0] * M for _ in range(N)]

print(bfs())