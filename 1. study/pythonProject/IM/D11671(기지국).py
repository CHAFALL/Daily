import sys
sys.stdin = open('D11671.txt')

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 기지국이면 검토 시작
            if arr[i][j] in ['A', 'B', 'C']:
                if arr[i][j] == 'A':
                    p = 1
                elif arr[i][j] == 'B':
                    p = 2
                elif arr[i][j] == 'C':
                    p = 3

                for k in range(4):
                    for q in range(1, p + 1): # 여기 조심!!!
                        ni = i + di[k] * q
                        nj = j + dj[k] * q
                        if 0<= ni < N and 0 <= nj < N:
                            # 만약 범위 내에 집이 있으면
                            if arr[ni][nj] == 'H':
                                arr[ni][nj] = 'X'

    # cover 안되는 집 검토
    counts = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                counts += 1

    print(f'#{tc} {counts}')



