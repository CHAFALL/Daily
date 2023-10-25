#[1, 2, 3] 모든 부분집합 2^3
# def powerset(n, k): # n: 원소의 갯수, k: 재귀의 깊이
#     if n == k:
#         print(bit, end=' ')
#         for i in range(n):
#             if bit[i]: print(arr[i], end=' ')
#         print()
#     else:
#         bit[k] = 1
#         powerset(n, k + 1)
#         bit[k] = 0
#         powerset(n, k + 1)
#
# arr = [1, 2, 3]
# N = len(arr)
# bit = [0] * N #원소의 포함 여부(0, 1)
# powerset(N, 0)
#------------------------------------------------------------
# 부분집합의 합이 10인 부분집합 찾기
# def powerset(n, k): # n: 원소의 갯수, k: 재귀의 깊이
#     global count, total
#     total += 1
#     if n == k: # 여기서 수정
#         # 부분집합의 합
#         sum = 0
#         for i in range(n):
#             if bit[i]:
#                 sum += arr[i]
#         # 합이 10일때 출력
#         if sum == 10:
#             count += 1
#             for i in range(n):
#                 if bit[i]:
#                     print(arr[i], end=' ')
#             print()
#     else:
#         bit[k] = 1
#         powerset(n, k + 1)
#         bit[k] = 0
#         powerset(n, k + 1)
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# N = len(arr)
# bit = [0] * N #원소의 포함 여부(0, 1)
# count = 0
# total = 0
# powerset(N, 0)
# print(f'count={count}, 호출횟수={total}')

#==============================================================
# 부분집합 가지치기
# def powerset(n, k, cursum): # n: 원소의 갯수, k: 재귀의 깊이 cursum: 현재까지의 합
#     global count, total
#     total += 1
#     if cursum > 10:
#         return
#     if n == k:
#         # 합이 10일때 출력
#         if cursum == 10:
#             count += 1
#             for i in range(n):
#                 if bit[i]:
#                     print(arr[i], end=' ')
#             print()
#     else:
#         bit[k] = 1
#         powerset(n, k + 1, cursum + arr[k])
#         bit[k] = 0
#         powerset(n, k + 1, cursum)
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# N = len(arr)
# bit = [0] * N  #원소의 포함 여부(0, 1)
# count = 0
# total = 0
# powerset(N, 0, 0)
# print(f'count={count}, 호출횟수={total}')
#
# # 주의 할당(=)을 하지말고 (+=)or(+)로 할 것(cursum 변수 만들고),\
# # 되돌아올때 저장이 안 되어 있어서\
# # 사라지므로 (cursum에서)
#-------------------------------------------------------------------------
# 순열(nPn)
# def perm(n, k):
#     if n == k:
#         print(arr) # 이거 잘 생각해보면 이해도 up(함수 스택)
#         return
#     else:
#         for i in range(k, n):
#             arr[k], arr[i] = arr[i], arr[k] # 아래의 함수 들어가기 전 실행
#             perm(n, k+1)
#             arr[k], arr[i] = arr[i], arr[k] # 복구, 나온 뒤 실행(위의 함수 return 하면서)

# arr = [1, 2, 3]
# N = len(arr)
# perm(N, 0)


#===================================================================
# # 순열(nPn) 가지치기 위치
# def perm(n, k, s):
#     ######################## 가지치기
#     if n == k:
#         print(arr)
#         return
#     else:
#         for i in range(k, n):
#             arr[k], arr[i] = arr[i], arr[k]
#             perm(n, k+1, s+arr[])
#             arr[k], arr[i] = arr[i], arr[k] # 복구
#
# arr = [1, 2, 3]
# N = len(arr)
# perm(N, 0)