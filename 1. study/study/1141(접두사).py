


# 부분집합(비트마스킹, 그룹 나누기)(반)(공집합 x)
# arr = [1,2,3,4]
# N = len(arr)
# for i in range(1, 1 << (N - 1)):
#     subset1 = []
#     subset2 = []
#     for j in range(N):
#         if i & (1 << j):
#             subset1.append(arr[j])
#         else:
#             subset2.append(arr[j])
#
#     print(subset1, subset2)

# 부분집합 구하기
# def powerset(k, p):
#
#     if k == N:
#         print(p)
#         return
#     else:
#         powerset(k + 1, p + [arr[k]])
#         powerset(k + 1, p)
#

#
# powerset(0, [])


#--------------------------------------------

N = int(input())
arr = [input() for _ in range(N)]

# 긴 놈은 짧은 놈의 접두사가 될 수 x
# 길이 순 나열하기
arr.sort(key=len)

ans = arr[:]
for i in range(N):
    # 나보다 긴 놈만 비교하면 돼!
    for j in range(i + 1, N):
        if arr[j].startswith(arr[i]):
            ans.remove(arr[i])
            break

print(len(ans))

#--------------------------------------

N = int(input())
arr = [input() for _ in range(N)]

# 긴 놈은 짧은 놈의 접두사가 될 수 x
# 길이 순 나열하기
arr.sort(key=len)

ans = arr[:]
for i in range(N):
    # 나보다 긴 놈만 비교하면 돼!
    for j in range(i + 1, N):
        # 접두사 체크
        if arr[i] ==arr[j][0:len(arr[i])]:
            ans.remove(arr[i])
            break

print(len(ans))

