# 순열 구하는 함수(파이썬만 있어서 쓰지 마시오)
# import math
# print(math.perm(3)) # 순열 갯수 알려줌
# print(math.comb(4, 3)) # 조합 갯수 알려줌
#----------------------------------------------------
# 조합
# def comb(n, r):
#     if r == 0:
#         print(T)
#     elif n < r:
#         return
#     else:
#         T[r-1] = A[n-1]
#         comb(n - 1, r - 1)
#         comb(n - 1, r)
#
# A = [1, 2, 3, 4]
# N = len(A)
# R = 3
# T = [0] * R
# comb(N, R)
#-----------------------------------------------
# 중복 조합
# def comb(n, r):
#     if r == 0:
#         print(T)
#     elif n == 0: # 여기랑
#         return
#     else:
#         T[r-1] = A[n-1]
#         comb(n, r - 1) # 여기만 바꾸면 된다.
#         comb(n - 1, r)
#
# A = [1, 2, 3, 4]
# N = len(A)
# R = 3
# T = [0] * R
# comb(N, R)
#--------------------------------------------------
# 조합 갯수 구하기
# def comb(n, r):
#     if r == 0:
#         return 1
#     elif n < r: # 여기랑
#         return 0
#     else:
#         return comb(n-1, r-1) + comb(n-1, r)
#
# print(comb(4, 3))
#----------------------------------------------------
# for 로 구현 해보기
# 고르는 갯수가 정해져 있을때 쓰임 (재귀보다 for문이 빠르므로)
# a = [1, 2, 3, 4]
# N = len(a)
# for i in range(N - 2):
#     for j in range(i + 1, N - 1):
#         for k in range(j+1, N):
#             print(a[i], a[j], a[k])
#
# print('-----------------------------------------------')
# # 재귀로 위의 것 구현하기
# def comb(n, r, k, s): # s는 시작 숫자
#     if r == k:
#         print(T)
#     else:
#         for i in range(s, n - r + 1 + k): # n - r + 1 :선택할 수 있는 마지막 원소
#             T[k] = a[i]
#             comb(n, r, k+1, i+1)
#
# a = [1, 2, 3, 4]
# N = len(a)
# R = 3
# T = [0] * R
# comb(N, R, 0, 0)
#---------------------------------------------------------------------
# 위의 것에서 중복 포함
def comb(n, r, k, s): # s는 시작 숫자
    if r == k:
        print(T)
    else:
        for i in range(s, n):
            T[k] = a[i]
            comb(n, r, k+1, i)

a = [1, 2, 3, 4]
N = len(a)
R = 3
T = [0] * R
comb(N, R, 0, 0)