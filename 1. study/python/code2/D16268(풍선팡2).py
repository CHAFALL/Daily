import sys
sys.stdin = open('D16268.txt')

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     di = [0, -1, 0, 1]
#     dj = [-1, 0, 1, 0]
#
#     max_v = 0
#     for i in range(N):
#         for j in range(M):
#             total = arr[i][j]
#             for k in range(4):
#                 ni = i + di[k]
#                 nj = j + dj[k]
#
#                 if 0 <= ni < N and 0 <= nj < M:
#                     total += arr[ni][nj]
#
#             if max_v < total:
#                 max_v = total
#     print(f'#{tc} {max_v}')
#
#--------------------------------------------------------
#연습
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, -1, 0, 1]
    dj = [-1, 0, 1, 0]

    max_total = 0
    for i in range(N):
        for j in range(M):
            total = arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]

                if 0<= ni < N and 0<= nj < M:
                    total += arr[ni][nj]
            if max_total < total:
                max_total = total
    print(max_total)