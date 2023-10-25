# def comb(n, r, k, s): # s는 시작 숫자
#     if r == k:
#         print(*p)
#     else:
#         for i in range(s, n - r + 1 + k): # n - r + 1 :선택할 수 있는 마지막 원소
#             p[k] = arr[i]
#             comb(n, r, k+1, i+1)
#
#
# N, M = map(int, input().split())
# arr = list(range(1, N+1))
# p = [0] * M
# comb(N, M, 0, 0)
#

#----------------------------------------------------------------------------------

# 지환이 방식
# def comb(n, r, p):
#     if n == N: # 왜 이렇게 해야하는가? 그래야 n == N일때 리턴하겠지?
#         if r == M:
#             print(*p)
#         return
#
#     comb(n + 1, r + 1, p + [A[n]])
#     comb(n + 1, r, p)
#
# N, M = map(int, input().split())
# A = list(range(1, N+1))
#
# comb(0, 0, [])