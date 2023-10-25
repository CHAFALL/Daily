import sys
sys.stdin = open('D1216.txt')

# T = 10
# N = 100
# for _ in range(1, T+1):
#     tc = int(input())
#     text = [list(input()) for _ in range(N)]
#
#     # 행
#     length = 0
#     for r in range(N):
#         for k in range(1, N+1): # 회문의 길이
#             for i in range(N-k+1):
#                 flag = 1
#                 for j in range(k // 2):
#                     if text[r][i+j] != text[r][i+k-1-j]:
#                         flag = 0
#                         break
#                 if flag:
#                     if length < k:
#                         length = k
#
#     # 열
#     for c in range(N):
#         for k in range(1, N + 1):  # 회문의 길이
#             for i in range(N - k + 1):
#                 flag = 1
#                 for j in range(k // 2):
#                     if text[i + j][c] != text[i + k - 1 - j][c]:
#                         flag = 0
#                         break
#                 if flag:
#                     if length < k:
#                         length = k
#
#     print(f'#{tc} {length}')
#


#------------------------------------------------------------------------------
# 연습
N = 100
T = 10
for _ in range(1, T+1):
    tc = int(input())
    text = [input() for _ in range(N)]
    # 행
    max_v = 0
    for r in range(N):
        for k in range(1, N+1):
            for i in range(N - k + 1):
                flag = 1
                for j in range(k // 2):
                    if text[r][i+j] != text[r][i + k - 1 -j]:
                        flag = 0
                        break
                if flag:
                    if max_v < k:
                        max_v = k

    # 열
    for c in range(N):
        for k in range(1, N + 1):
            for i in range(N - k + 1):
                flag = 1
                for j in range(k // 2):
                    if text[i + j][c] != text[i + k - 1 - j][c]:
                        flag = 0
                        break
                if flag:
                    if max_v < k:
                        max_v = k

    print(max_v)






