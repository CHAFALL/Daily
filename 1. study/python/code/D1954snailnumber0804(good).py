import sys
sys.stdin = open('D1954')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    i, j = 0, 0
    k = 0
    num = 1
    while num < N ** 2 + 1:
        arr[i][j] = num
        ni = i + di[k]
        nj = j + dj[k]

        if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] != 0:
            k = (k+1) % 4
            ni = i + di[k]
            nj = j + dj[k]

        i = ni
        j = nj
        num += 1

    print(f'#{tc}')
    for p in arr:
        print(*p)