import sys
sys.stdin = open('D11883.txt')
# def perm(N, K, cursum):
#     global ans
#
#     if ans <= cursum:
#         return
#
#     if N == K:
#         if ans > cursum:
#             ans = cursum
#
#     else:
#         for i in range(K, N):
#             A[K], A[i] = A[i], A[K]
#             perm(N, K+1, cursum + arr[K][A[K]])
#             A[K], A[i] = A[i], A[K]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     A = list(range(N))
#     ans = 1000
#     perm(N, 0, 0)
#     print(ans)

#------------------------------------------------------------------
# 연습
