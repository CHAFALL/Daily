import sys
sys.stdin = open('D11886.txt')

def find_two():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j

def bfs(v1, v2):
    global ans
    Q = []
    Q.append((v1, v2))
    visited[v1][v2] = 1

    while Q:
        i, j = Q.pop()
        if arr[i][j] == 3:
            ans += visited[i][j] -2
            return
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0<= nj < N and arr[ni][nj] != 1\
                and visited[ni][nj] == 0:
                Q.append((ni, nj))
                visited[ni][nj] += visited[i][j] + 1
    return

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ans = 0
    si, sj = find_two()
    bfs(si, sj)
    print(ans)

