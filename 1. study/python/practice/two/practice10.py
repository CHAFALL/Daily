#  nPn 순열 (순서대로 버전)
# def perm(n, k): # n은 원소갯수, k : depth
#     if n == k:
#         print(p)
#         # return (맨 끝이라 생략가능??)
#     else:
#         for i in range(n):
#             if visited[i] == 0:
#                 visited[i] = 1
#                 p[k] = a[i]
#                 perm(n, k+1)
#                 visited[i] = 0
#
# a =[1, 2, 3]
# N = len(a)
# p = [0] * N
# visited = [0] * N
# perm(N, 0)

#--------------------------------------------------
# #  nPr 순열 (순서대로 버전)
# def perm(n, k, r): # n은 원소갯수, k : depth
#     if r == k:
#         print(p)
#         # return (맨 끝이라 생략가능??)
#     else:
#         for i in range(n):
#             if visited[i] == 0:
#                 visited[i] = 1
#                 p[k] = a[i]
#                 perm(n, k+1, r)
#                 visited[i] = 0
#
# a =[1, 2, 3]
# N = len(a)
# R = 2
# p = [0] * R
# visited = [0] * N
# perm(N, 0, R)
#----------------------------------------------------------
# # 중복 순열 nㅠn (visited 주석 처리만 하면 된다.)
# def perm(n, k): # n은 원소갯수, k : depth
#     if n == k:
#         print(p)
#     else:
#         for i in range(n):
#             # if visited[i] == 0:
#             #     visited[i] = 1
#                 p[k] = a[i]
#                 perm(n, k+1)
#                 # visited[i] = 0
#
# a =[1, 2, 3]
# N = len(a)
# p = [0] * N
# # visited = [0] * N
# perm(N, 0)
#--------------------------------------------------
# # nㅠr 순열 (visited 주석 처리만 하면 된다.)
# def perm(n, k, r): # n은 원소갯수, k : depth
#     if r == k:
#         print(p)
#         # return (맨 끝이라 생략가능??)
#     else:
#         for i in range(n):
#             # if visited[i] == 0:
#                 # visited[i] = 1
#                 p[k] = a[i]
#                 perm(n, k+1, r)
#                 # visited[i] = 0
#
# a =[1, 2, 3]
# N = len(a)
# R = 2
# p = [0] * R
# # visited = [0] * N
# perm(N, 0, R)

#--------------------------------------------------
# (일부만 순열 돌리기) (뺑 돌고 되돌아 오는 경우에 이용됨)
def perm(n, k): # n은 원소갯수, k : depth
    if n == k:
        print(p)
        # return
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = a[i]
                perm(n, k+1)
                visited[i] = 0

a =[1, 2, 3, 4]
N = len(a)
# (고정하는 방법)(1번 고정 case)
p = [0] * (N + 1)
p[0] = p[N] = a[0] # 출발점 하고 도착점 같아졌다
visited = [0] * N
visited[0] = 1
perm(N, 1)