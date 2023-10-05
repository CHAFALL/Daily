import sys
sys.stdin = open('D11315.txt')

# 오른쪽, 오른쪽 아래, 아래, 왼쪽 아래
# 행, 열, 양쪽 대각선 느낌
# di = [0, 1, 1, 1]
# dj = [1, 1, 0, -1]
#
# def solve():
#     for i in range(N):
#         for j in range(N):
#             # 돌 있으면 4방향 탐색
#             if arr[i][j] == 'o':
#                 for k in range(4):
#                     p = 1
#                     counts = 1  # 이미 하나 찾았으므로
#                     while True:
#                         ni = i + di[k] * p
#                         nj = j + dj[k] * p
#                         if 0 <= ni < N and 0 <= nj < N:
#                             # 또 돌이 있으면
#                             if arr[ni][nj] =='o':
#                                 counts += 1
#                                 p += 1
#                                 # 오목 이면
#                                 if counts >= 5: # 여기 실수 주의
#                                     return 'YES'
#                             else:
#                                 break
#
#                         else:
#                             break
#     return 'NO'
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(input()) for _ in range(N)]
#
#     print(f'#{tc} {solve()}')
#------------------------------------------------------------------
# 연습
# di = [0, 1, 1, 1]
# dj = [1, 1, 0, -1]
# T = int(input())
#
#
# def solve():
#     for i in range(N):
#         for j in range(N):
#             # 돌이면 탐색 시작
#             if arr[i][j] == 'o':
#
#                 for k in range(4):
#                     p = 1
#                     cnt = 1
#                     while True:
#                         ni = i + di[k] * p
#                         nj = j + dj[k] * p
#                         if 0 <= ni < N and 0 <= nj < N:
#                             if arr[ni][nj] == 'o':
#                                 cnt += 1
#                                 p += 1
#                                 if cnt >= 5:
#                                     return 'YES'
#                             else:
#                                 break
#                         else:
#                             break
#     return 'NO'
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(input()) for _ in range(N)]
#     ans = 'NO'
#
#     print(solve())