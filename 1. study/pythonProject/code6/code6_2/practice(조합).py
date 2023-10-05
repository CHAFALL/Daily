# 조합 nCr(이건 좀 더 연구 필요)
# def comb(n, r):
#     if r == 0:
#         print(p)
#         return
#     elif n < r: # 남은 원소보다 많은 원소를 선택해야 하는 경우
#         return
#     else:
#         p[r - 1] = arr[n - 1] # arr[n-1]을 조합에 포함시키는 경우
#         comb(n-1, r-1)
#         comb(n-1, r) # arr[n-1]을 포함시키지 않는 경우
#
# arr = [1, 2, 3, 4, 5]
# N = len(arr)
# R = 3
# p = [0] * R
# comb(N, R)

#------------------------
# 조합 nCr (이게 지환이 방식인가?)(중복 포함이면 못 만드나?)(순열 불가)
# def comb(k, p):
#     global cnt
#     if k == N:
#         if len(p) == R:
#             cnt += 1
#             print(p, cnt)
#         return
#     comb(k+1, p+[arr[k]])
#     comb(k+1, p)
#
#
# cnt = 0
# arr = [1, 2, 3, 4, 5]
# N = 5
# R = 3
# comb(0, [])
#-------------------------------------------------
# 중복 조합(이것도 연구 필요)
# def comb(n, r):
#     if r == 0:
#         print(p)
#         return
#     elif n == 0:
#         return
#     else:
#         p[r - 1] = arr[n - 1]
#         comb(n, r - 1)
#         comb(n - 1, r)
#
# arr = [1, 2, 3, 4, 5]
# N = len(arr)
# R = 3
# p = [0] * R
# comb(N, R)
#----------------------------------------------
# nCr for로 구현 (갯수가 정해져 있을 때 좋음)
# arr = [1,2,3,4,5]
# N = len(arr)
# # R = 3
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             print(arr[i], arr[j], arr[k])
#-------------------------------------------
# nCr 위의 것을 재귀로 구현(이거 좋다.)
# def comb(k, s):  # s는 시작 숫자
#     if k == R:
#         print(p)
#         return
#     else:
#         for i in range(s, N - R + 1 + k):  # N - R + 1: 선택할 수 있는 마지막 원소
#             p[k] = arr[i]
#             comb(k + 1, i + 1)
#
#
# arr = [1, 2, 3, 4, 5]
# N = len(arr)
# R = 3
# p = [0] * R
# comb(0, 0)
#----------------------------------------------------
# nCr 재귀 이면서 중복 포함(이것도 기억해두기)
def comb(k, s):
    if k == R:
        print(p)
        return
    else:
        for i in range(s, N):
            p[k] = arr[i]
            comb(k + 1, i)  # 여기도 i로 바꿔줘야 됨


arr = [1, 2, 3, 4]
N = len(arr)
R = 3
p = [0] * R
comb(0, 0)
#-------------------------------------------------------

