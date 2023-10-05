# 순열 nPn 근데 이 방식은 별로라 카던데??
# def perm(k):
#     if k == N:
#         print(arr)
#         return
#     for i in range(k, N):
#         arr[k], arr[i] = arr[i], arr[k]
#         perm(k + 1)
#         arr[k], arr[i] = arr[i], arr[k]
#
#
# arr = [i for i in range(1, 4)]
# N = len(arr)
# perm(0)
#--------------------------------------------------
# 순열 nPn
# def perm(k):
#     if k == N:
#         print(p)
#         return
#     for i in range(N):
#         if not visited[i]:
#             p[k] = arr[i]
#             visited[i] = 1
#             perm(k + 1)
#             visited[i] = 0
#
#
# arr = [1,2,3]
# N = 3
# p = [0] * N
# visited = [0] * N
# perm(0)

#---------------------------------------------
# 순열 nPr
# def perm(k):
#     if k == R:
#         print(p)
#         return
#     else:
#         for i in range(N):
#             if visited[i] == 0:
#                 p[k] = arr[i]
#                 visited[i] = 1
#                 perm(k + 1)
#                 visited[i] = 0
#
#
# arr = [1, 2, 3, 4, 5]
# N = 5
# R = 3
# visited = [0] * N  # 사용여부 파악하기
# p = [0] * R  # 내가 채울 칸
# perm(0)

#------------------------------------------
# nㅠn (중복 순열)
# def perm(k):
#     if k == N:
#         print(p)
#         return
#     for i in range(N):
#         p[k] = arr[i]
#         perm(k + 1)
#         # p[k] = 0 이거 왜 있으나 없으나 같지?
#
#
# arr = [1, 2, 3]
# N = 3
# p = [0] * N
# perm(0)
#---------------------------------------------------
# nㅠr (중복 순열)
# def perm(k):
#     if k == R:
#         print(p)
#         return
#     for i in range(N):
#         p[k] = arr[i]
#         perm(k + 1)
#
# arr = [1, 2, 3, 4, 5]
# N = 5
# R = 3
# p = [0] * R
# perm(0)

#--------------------------------------------------------------------
#nPr 순열(visited 안 쓰고 하기)(음... 좀 더 연구 필요)
#
# def perm(k):
#     if k == N:
#         print(*p)
#         return
#
#     for num in arr:
#         if num in p:
#             continue
#
#         # 들어가기 전 로직 - 경로 저장
#         p[k] = num
#         # 다음 재귀 함수 호출
#         perm(k + 1)
#         # 돌아와서 할 로직
#         p[k] = 0  # 이전에 선택했던 상태가 남아있으면 안됨(초기화)
#
#
# arr = [i for i in range(1, 4)]
# N = 3
# p = [0] * 3
# perm(0)

