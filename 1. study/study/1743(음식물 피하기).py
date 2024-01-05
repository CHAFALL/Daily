import sys
sys.setrecursionlimit(10**6)

def dfs(i, j):
    global cnt
    arr[i][j] = 9  # 방문체크
    # 하고 싶은 일
    cnt += 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1:
            dfs(ni, nj)


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1

max_value = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cnt = 0  # 현재 음식물 수
            dfs(i, j)
            max_value = max(max_value, cnt)

print(max_value)


