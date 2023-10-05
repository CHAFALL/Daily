import sys
sys.stdin = open('D1209')

T = 10
N = 100
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    # 행 우선 합 구하기
    for i in range(N):
        temp = 0
        for j in range(N):
            temp += arr[i][j]

        if max_v < temp:
            max_v = temp

    # 열 우선 합 구하기
    for j in range(N):
        temp = 0
        for i in range(N):
            temp += arr[i][j]

        if max_v < temp:
            max_v = temp

    # 오른쪽 대각선 합 구하기
    temp = 0
    for i in range(N):
        temp += arr[i][i]

    if max_v < temp:
        max_v = temp

    # 왼쪽 대각선 합 구하기
    temp = 0
    for i in range(N-1, -1, -1):
        temp += arr[i][i]

    if max_v < temp:
        max_v = temp

    print(f'#{tc} {max_v}')




