import sys
sys.stdin = open('D9490.txt')


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(M):
            temp = arr[i][j]
            for k in range(4):
                for p in range(1, arr[i][j] + 1):
                    ni = i + di[k] * p
                    nj = j + dj[k] * p
                    if 0<= ni < N and 0<= nj < M:
                        temp += arr[ni][nj]

            if max_v < temp:
                max_v = temp

    print(max_v)


