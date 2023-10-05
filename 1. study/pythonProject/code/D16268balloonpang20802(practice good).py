import sys
sys.stdin = open('D16268')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # # 방법 1(비추, 2차원 배열 만들시엔 아래 방법이 나음)
    # arr = []
    # for _ in range(N):
    #     arr.append(list(map(int, input().split())))

    #방법 2
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, -1, 0, 1]
    dj = [-1, 0, 1, 0]

    real_max_v = 0
    for i in range(N):
        for j in range(M):
            max_v = arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    max_v += arr[ni][nj]

            if real_max_v < max_v:
                real_max_v = max_v

    print(f'#{tc} {real_max_v}')


