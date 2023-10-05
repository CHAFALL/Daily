import sys
sys.stdin = open('D14889')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 0, 0, 1]
    dj = [0, -1, 1, 0]

    max_v = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    temp = arr[ni][nj] - arr[i][j]
                    if temp > 0:
                        max_v += temp
                    else:
                        max_v -= temp

    print(f'#{tc} {max_v}')

