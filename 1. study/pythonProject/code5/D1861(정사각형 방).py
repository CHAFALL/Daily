import sys
sys.stdin = open('D1861.txt')

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_cnt = 0
#     max_start = 0
#     for p in range(N):
#         for q in range(N):
#             i, j = p, q
#             cnt = 1
#             start = arr[i][j]
#
#             while True:
#                 for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#                     ni, nj = i + di, j + dj
#                     if 0 <= ni < N and 0 <= nj < N and arr[i][j] + 1 == arr[ni][nj]:
#                         cnt += 1
#                         i, j = ni, nj
#                         break
#                 else:
#                     break
#             if max_cnt < cnt:
#                 max_cnt = cnt
#                 max_start = start
#             elif max_cnt == cnt and max_start > start:
#                 max_start = start
#     print(f'#{tc} {max_start} {max_cnt}')

#------------------------------------------------------------------------------
# 그리디 방식 (카운트 방식으로 주면에 1 차이나는것이 있니?로 하고 연속된 것의 max 찾으면 되는듯)
#(그리고 연속된 것 찾을 때도 인덱스 뒤에서 부터 하면 좀 더 good)

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     C = [0] *(N * N + 1) # 연속으로 1이 커지는 경우를 표시할 배열
#     for i in range(N):
#         for j in range(N):
#             for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#                 ni, nj = i + di, j + dj # arr[i][j]의 주변 칸이
#                 if 0 <= ni < N and 0 <= nj < N and arr[i][j] + 1 == arr[ni][nj]:
#                     C[arr[i][j]] += 1
#
#     max_cnt = 0
#     max_start = 0
#     cnt = 0
#     for k in range(N * N, 0, -1):
#         if C[k]:
#             cnt += 1
#             if max_cnt < cnt:
#                 max_cnt = cnt
#                 max_start = k
#             elif max_cnt == cnt:
#                 max_start = k
#
#         else:
#             cnt = 0
#     print(f'#{tc} {max_start} {max_cnt + 1}')

#-----------------------------------------------------------------
# 연습

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = 0
    max_start = 0
    for p in range(N):
        for q in range(N):
            i = p # 인덱스 망가지는 것 영향 안 줄려고
            j = q
            cnt = 1
            start = arr[i][j]

            while True:
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and arr[i][j] + 1 == arr[ni][nj]:
                        cnt += 1
                        i = ni
                        j = nj
                        break
                else:
                    break

            if max_cnt < cnt:
                max_cnt = cnt
                max_start = start

            elif max_cnt == cnt and max_start > start:
                max_start = start

    print(f'#{tc} {max_start} {max_cnt}')








