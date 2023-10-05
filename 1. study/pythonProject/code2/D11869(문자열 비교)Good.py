import sys
sys.stdin = open('D11869.txt')

T = int(input())
for tc in range(1, T+1):
    pattern = input()
    text = input()

    M = len(pattern)
    N = len(text)

    ans = 0
    i = 0
    j = 0
    while i < N and j < M:
        if text[i] != pattern[j]:
            i -= j
            j = -1

        i += 1
        j += 1
    if j == M:
        ans = 1

    print(f'#{tc} {ans}')

#=========================================================
# # for문으로 구현
# T = int(input())
# for tc in range(1, T+1):
#     pattern = input()
#     text = input()
#
#     M = len(pattern)
#     N = len(text)
#
#     for i in range(N-M+1):
#         flag = 1
#         for j in range(M):
#             if text[i+j] != pattern[j]:
#                 flag = 0
#                 break
#
#         if flag == 1: # 이거 안해주면 안됨!!!! 마지막 것으로 되므로
#             break
#
#
#     print(f'#{tc} {flag}')
#----------------------------------------------------------------------------
# 연습
# def check(pattern, text):
#
#     for i in range(N-M+1):
#         flag = 1
#         for j in range(M):
#             if text[i+j] != pattern[j]:
#                 flag = 0
#                 break
#         if flag:
#             return 1
#     return 0
#
#
# T = int(input())
# for tc in range(1, T+1):
#     pattern = input()
#     text = input()
#
#     M = len(pattern)
#     N = len(text)
#
#     print(check(pattern, text))

#-------------------------------------------------------------------------
# 연습2
# T = int(input())
# for tc in range(1, T+1):
#     pattern = input()
#     text = input()
#
#     M = len(pattern)
#     N = len(text)
#
#     i = 0
#     j = 0
#     ans = 0
#     while i < N and j < M:
#         if pattern[j] != text[i]:
#             i -= j
#             j = -1
#
#         i += 1
#         j += 1
#
#         if j == M:
#             ans = 1
#
#     print(ans)


