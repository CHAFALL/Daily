import sys
sys.stdin = open('D11673.txt')

# 0:오른쪽 1:아래 2:왼쪽 3:위
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    i, j = 0, 0
    k = 0
    counts = 0
    while True:
        ni = i + di[k]
        nj = j + dj[k]
        # 인덱스 조건
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == 1 and k == 0:
                k = 3
                counts += 1
            elif arr[ni][nj] == 1 and k == 1:
                k = 2
                counts += 1
            elif arr[ni][nj] == 1 and k == 2:
                k = 1
                counts += 1
            elif arr[ni][nj] == 1 and k == 3:
                k = 0
                counts += 1
            elif arr[ni][nj] == 2 and k == 0:
                k = 1
                counts += 1
            elif arr[ni][nj] == 2 and k == 1:
                k = 0
                counts += 1
            elif arr[ni][nj] == 2 and k == 2:
                k = 3
                counts += 1
            elif arr[ni][nj] == 2 and k == 3:
                k = 2
                counts += 1

            i = ni
            j = nj

        else:
            break
    print(f'#{tc} {counts}')