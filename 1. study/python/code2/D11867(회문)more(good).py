import sys
sys.stdin = open('D11867.txt')

# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     text = [input() for _ in range(N)]
#
#     print(f'#{tc} ', end='')
#     # 행
#     for r in range(N):
#
#         for i in range(N-M+1):
#             flag = 1
#             for j in range(M // 2):
#                 if text[r][i+j] != text[r][i+M-1-j]:
#                     flag = 0
#
#             if flag == 1:
#                 for j in range(M):
#                     print(f'{text[r][i+j]}', end ='')
#                 print()
#
#     # 열
#     for c in range(N):
#         for i in range(N - M + 1):
#             flag = 1
#             for j in range(M // 2):
#                 if text[i + j][c] != text[i + M - 1 - j][c]:
#                     flag = 0
#
#             if flag == 1:
#                 for j in range(M):
#                     print(f'{text[i + j][c]}', end='')
#                 print()
#
#
#
#------------------------------------------------------
# 연습
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    text = [input() for _ in range(N)]
    # 행
    ans = 0
    for r in range(N):
        for i in range(N-M+1):
            flag = 1
            for j in range(M // 2):
                if text[r][i+j] != text[r][i+M-1-j]:
                    flag = 0
                    break
            if flag:
                for j in range(M):
                    print(text[r][i+j], end='')
                print()


    # 열
    for c in range(N):
        for i in range(N-M+1):
            flag = 1
            for j in range(M // 2):
                if text[i+j][c] != text[i+M-1-j][c]:
                    flag = 0
                    break
            if flag:
                for j in range(M):
                    print(text[i+j][c], end='')
                print()


