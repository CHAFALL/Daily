import sys
sys.stdin = open('D1227.txt')

def solve(v1, v2, arr):
    global flag
    Q = []
    Q.append((v1, v2)) # 올리고
    visited[v1][v2] = 1 # 방문체크

    while Q:
        i, j = Q.pop(0)
        if arr[i][j] == 3:
            flag = 1
            return
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1\
                and visited[ni][nj] == 0:
                Q.append((ni, nj))
                visited[ni][nj] += 1
    return

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


N = 100
T = 10
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    flag = 0
    solve(1, 1, arr)
    print(flag)

#---------------------------------------------------------------------
#연습

