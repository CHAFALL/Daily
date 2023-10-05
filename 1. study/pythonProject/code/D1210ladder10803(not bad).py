import sys
sys.stdin = open('D1210')
N = 100
T = 10
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 2 구하기
    for j in range(N):
        if arr[99][j] == 2:
            finish_j = j
            break
    i = 99
    di = [0, 0, -1]
    dj = [-1, 1, 0]

    while i > 0: # while문 필요
        for k in range(3):
            ni = i + di[k]
            nj = finish_j + dj[k]
            if 0<= ni < N and 0<= nj < N and arr[ni][nj] == 1:
                i = ni
                finish_j = nj
                arr[i][finish_j] = 9 # 퇴로 막기
                break

    print(f'#{tc} {finish_j}')




