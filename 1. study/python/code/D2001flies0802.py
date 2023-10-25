import sys
sys.stdin = open('D2001')

T= int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    real_max_v = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            max_v = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    max_v += arr[x][y]

            if real_max_v < max_v:
                real_max_v = max_v

    print(f'#{tc} {real_max_v}')


