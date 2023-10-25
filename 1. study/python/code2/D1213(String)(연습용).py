import sys
sys.stdin = open('D1213.txt', encoding='UTF8')
# for로 풀기
# T = 10
# for _ in range(1, T+1):
#     tc = int(input())
#     pattern = input()
#     text = input()
#
#     N = len(text)
#     M = len(pattern)
#
#     ans = 0
#     for i in range(N-M+1):
#         flag = 1
#         for j in range(M):
#             if text[i+j] != pattern[j]:
#                 flag = 0
#                 break
#         if flag == 1:
#             ans +=1
#
#     print(f'#{tc} {ans}')
#--------------------------------------------------------
#while로 풀기
# T = 10
# for _ in range(1, T+1):
#     tc = int(input())
#     pattern = input()
#     text = input()
#
#     N = len(text)
#     M = len(pattern)
#
#     i = 0
#     j = 0
#     counts = 0
#     while i < N:
#         if text[i] != pattern[j]:
#             i -= j
#             j = -1
#
#         i += 1
#         j += 1
#
#         if j == M:
#             counts += 1
#             j = 0
#
#     print(f'#{tc} {counts}')


#-----------------------------------------------------
# def my_find(t, p):
#     global ans
#     for i in range(len(t) - len(p) + 1):  # text
#         flag = 1
#         for j in range(len(p)):  # pattern
#             if t[i + j] != p[j]:
#                 flag = 0
#                 break
#         if flag:
#             ans += 1
#
#
# T = 10
# for tc in range(1, T + 1):
#     no = int(input())
#     pattern = input()
#     text = input()
#     ans = 0
#     my_find(text, pattern)
#     print(f'#{tc} {ans}')

#------------------------------------------------------------------
# 연습
T = 10
for _ in range(1, T+1):
    tc = int(input())
    pattern = input()
    text = input()

    N = len(text)
    M = len(pattern)

    counts = 0
    for i in range(N-M+1):
        flag = 1
        for j in range(M):
            if pattern[j] != text[i+j]:
                flag = 0
                break
        if flag == 1:
            counts += 1

    print(counts)



