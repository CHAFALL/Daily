# 부분집합 부시기
# 1~9 부분집합 구하기(1번 방식)(별로인듯)
# def powerset(k):  # k:재귀의 깊이
#     if k == N:
#         print(bit)
#
#     else:
#         bit[k] = k + 1
#         powerset(k + 1)
#         bit[k] = 0
#         powerset(k + 1)
#
#
# N = 3
# # arr = [i for i in range(1, N + 1)]
# bit = [0] * N
# powerset(0)
#--------------------------------------------
# 1~9 부분집합 구하기(2번 방식)(이것도 pop써야 되어서 별로인듯)
# def powerset(k):  # k:재귀의 깊이
#     if k == N:
#         print(bit)
#
#     else:
#         bit.append(k + 1)
#         powerset(k + 1)
#         bit.pop()
#         powerset(k + 1)
#
#
# N = 3
# # arr = [i for i in range(1, N + 1)]
# bit = []
# powerset(0)
#----------------------------------------------------
# 1~9 부분집합 구하기(3번 방식)(좋은데??)
# def powerset(k, bit):  # k:재귀의 깊이
#     if k == N:
#         print(bit)
#
#     else:
#         powerset(k + 1, bit + [k + 1]) # 인덱스 1부터로 할려고
#         powerset(k + 1, bit)
#
#
# N = 3
# # arr = [i for i in range(1, N + 1)]
# bit = []
# powerset(0, bit)
#------------------------------------------------------
# 부분집합의 합이 10인 부분집합 찾기(1~10일 때)
# 이렇게 만드니 답은 맞는 것 같은데 직관적이지 않아서
# 아래에 좀 더 추가해서 만들어 보겠음
# def powerset(k, s):  # s: 합
#     global cnt
#     if k == N:
#         if s == 10:
#             cnt += 1
#         return
#
#     powerset(k + 1, s + arr[k])
#     powerset(k + 1, s)
#
#
#
# cnt = 0
# arr = [i for i in range(1, 11)]
# N = len(arr)
# powerset(0, 0)
# print(cnt)

#-----------------------------------------------------
# 부분집합의 합이 10인 부분집합 찾기(1~10일 때)(가지치기도?)
# def powerset(k, bit, s):
#     if 10 < s:
#         return
#
#     if k == N:
#         if s == 10:
#             print(bit, s)
#
#     else:
#         powerset(k + 1, bit + [arr[k]], s + arr[k])
#         powerset(k + 1, bit, s)
#
#
# arr = [i for i in range(1, 11)]
# N = len(arr)
# powerset(0, [], 0)
#---------------------------------------------------
# 부분집합의 합이 10인 부분집합 찾기(1~10일 때), 배열 없이 해보기
# 중복이 없으니깐 트리형식으로 하면 개 편하네..
# def powerset(k, bit, s):
#     if k == N:
#         if s == 10:
#             print(bit, s)
#         return
#     powerset(k + 1, bit + [k + 1], s + k + 1)
#     powerset(k + 1, bit, s)
#
# N = 10
# powerset(0, [], 0)
#---------------------------------------------------------
# 부분집합(비트 마스킹 이용)
# arr = [1,2,3,4]
# N = 4
# for i in range(1<<N):
#     subset = []
#     for j in range(N):
#         if i & (1<<j):
#             subset.append(arr[j])
#     print(subset)
#--------------------------------------------
# 부분집합(비트 마스킹 이용, 그룹 나누기)
# arr = [1,2,3,4]
# N = 4
# for i in range(1<<N):
#     subset1 = []
#     subset2 = []
#     for j in range(N):
#         if i & (1 << j):
#             subset1.append(arr[j])
#         else:
#             subset2.append(arr[j])
#
#     print(subset1, subset2)
#----------------------------------------------
# 부분집합(비트 마스킹 이용, 그룹 나누기), (공집합 x)
# arr = [1,2,3,4]
# N = 4
# for i in range(1, (1 << N)-1): # 생각해보면, 전부다 1이거나 전부다 0인 것 제거한 것임
#     subset1 = []
#     subset2 = []
#     for j in range(N):
#         if i & (1 << j):
#             subset1.append(arr[j])
#         else:
#             subset2.append(arr[j])
#
#     print(subset1, subset2)
#-------------------------------------------------------
# 부분집합(비트 마스킹 이용, 그룹 나누기), (공집합 x), (반으로 줄이기) (겹치니)
# arr = [1,2,3,4]
# N = 4
# for i in range(1, 1 << (N-1)): # 1<<(N - 1) == (1 << N) // 2
#     subset1 = []
#     subset2 = []
#     for j in range(N):
#         if i & (1 << j):
#             subset1.append(arr[j])
#         else:
#             subset2.append(arr[j])
#
#     print(subset1, subset2)