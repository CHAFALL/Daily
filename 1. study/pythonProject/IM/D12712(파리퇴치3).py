import sys
sys.stdin = open('D12712.txt')

# 상하좌우
di1 = [0, 1, 0, -1]
dj1 = [1, 0, -1, 0]
# 대각선
di2 = [-1, 1, 1, -1]
dj2 = [1, 1, -1, -1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(N):
            tmp = arr[i][j]
            for k in range(4):
                for p in range(1, M):
                    ni1 = i + di1[k] * p
                    nj1 = j + dj1[k] * p
                    if 0 <= ni1 < N and 0 <= nj1 < N:
                        tmp += arr[ni1][nj1]

            if max_v < tmp:
                max_v = tmp

    for i in range(N):
        for j in range(N):
            tmp = arr[i][j]
            for k in range(4):
                for p in range(1, M):
                    ni2 = i + di2[k] * p
                    nj2 = j + dj2[k] * p
                    if 0 <= ni2 < N and 0 <= nj2 < N:
                        tmp += arr[ni2][nj2]

            if max_v < tmp:
                max_v = tmp

    print(f'#{tc} {max_v}')