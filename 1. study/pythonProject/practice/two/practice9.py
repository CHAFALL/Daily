# def f(i, N): # i 현재 상태, N 목표
#     if i == N:
#         print(B)
#         return
#     else:
#         B[i] = A[i]
#         f(i+1, N)
#
# N = 5
# A = [1, 2, 3, 4, 5]
# B = [0] * N
# f(0, N)
# #-------------------------------------------
# #key가 있으면 1, 없으면 0을 리턴하는 함수
# def f(i, N, key, arr): # i 현재 상태, N 목표, key 찾고자 하는 원소
#     if i == N: # 내 생각: N-1이 아니라서 key가 5일때도 정상적?
#         return 0 # (N까지 가봤는데도) key가 없는 경우
#     elif arr[i] == key:
#         return 1
#     else:
#         return f(i+1, N, key, arr)
#
# N = 5
# A = [1, 2, 3, 4, 5]
# key = 5
# print(f(0, N, key, A)) # 1
#------------------------------------------------------------------
# 순열
#
# def f(i, N, K): # i 이전에 고른 개수, N개 에서 K개를 고르는 순열
#     global cnt
#     if i == K: # 순열 완성 : K개를 모두 고른 경우
#         cnt += 1
#         print(cnt, p)
#         return
#     else: # p[i]에 들어갈 숫자를 결정
#         for j in range(N):
#             if used[j] == 0: # 아직 사용되기 전이면
#                 p[i] = card[j]
#                 used[j] = 1
#                 f(i+1, N, K)
#                 used[j] = 0
#
# card = [1, 2, 3, 4, 5]
# N = 5  # N개의 숫자에서
# K = 4  # K개를 골라 만드는 순열
# used = [0] * N # 이미 사용한 카드인지 표시
# p = [0] * K # 내가 채울 칸
# cnt = 0
# f(0, N, K)
#------------------------------------------------------------
# # 공집합도 포함인 상태
# a = [1, 2, 3, 4]
# N = 4
# for i in range(1 << N):
#     subset1 = []
#     for j in range(N):
#         if i & (1 << j): # j번 비트가 0이 아니면
#             subset1.append(a[j])
#     print(*subset1)

#-----------------------------------------------------------
# 공집합도 포함인 상태이면서 0일때의 그룹과 1일때의 그룹으로 나누기
# a = [1, 2, 3, 4]
# N = 4
# for i in range(1 << N):
#     subset1 = []
#     subset2 = []
#     for j in range(N):
#         if i & (1 << j): # j번 비트가 0이 아니면
#             subset1.append(a[j])
#         else:
#             subset2.append(a[j])
#     print(subset1, subset2)

#----------------------------------------------------
# 하나도 없는 그룹이 없다면, 즉 공집합이 없다면?
# a = [1, 2, 3, 4]
# N = 4
# for i in range(1, (1 << N) - 1): # 여기 괄호 까먹지 말기!!
#     group1 = []
#     group2 = []
#     for j in range(N):
#         if i & (1 << j): # j번 비트가 0이 아니면
#             group1.append(a[j])
#         else:
#             group2.append(a[j])
#     print(group1, group2)
#-----------------------------------------------------
# 하나도 없는 그룹이 없다면, 즉 공집합이 없다면?, 자세히 보니 절반만 해도?
# a = [1, 2, 3, 4]
# N = 4
# for i in range(1, (1 << N) // 2): # 1<<(N - 1) == (1 << N) // 2
#     group1 = []
#     group2 = []
#     for j in range(N):
#         if i & (1 << j): # j번 비트가 0이 아니면
#             group1.append(a[j])
#         else:
#             group2.append(a[j])
#     print(group1, group2)

#-------------------------------------------------
# a = [3, 6, 7, 1, 5, 4]
# N = 6
# for i in range(1, (1 << N) // 2): # 1<<(N - 1) == (1 << N) // 2
#     group1 = []
#     group2 = []
#     total1 = 0
#     total2 = 0
#     for j in range(N):
#         if i & (1 << j): # j번 비트가 0이 아니면
#             group1.append(a[j])
#             total1 += a[j]
#         else:
#             group2.append(a[j])
#             total2 += a[j]
#
#     r1 = f(group1)
#     r2 = f(group2)
#     if r1 and r2:
#         if min_v > abs(total1 - total2)
#     print(group1, group2)