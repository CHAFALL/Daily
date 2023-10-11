# print(-1//2)
# print(int(-1/2))
# print(int(-1//2))


# 부분집합 만들기
# def powerset(k, p, s):
#     if k == N:
#         print(p, s)
#         return
#     else:
#         powerset(k + 1, p + [arr[k]], s + arr[k])
#         powerset(k + 1, p, s)
#
# arr = [1, 2, 3, 4, 5, 6, 7]
# N = len(arr)
# powerset(0, [], 0)
# 순열 만들기
# def perm(k, p):
#     if k == N:
#         print(p)
#         return
#     else:
#         for i in range(N):
#             if visited[i] == 0:
#                 visited[i] = 1
#                 perm(k+1, p+[arr[i]])
#                 visited[i] = 0
#
# arr = [1, 2, 3, 4]
# N = len(arr)
# visited = [0] * N
# perm(0, [])

# 조합 만들기
def comb(k, s, p, cur):
    if k == R:
        print(p, cur)
        return
    else:
        for i in range(s, N-R+1+k):
            comb(k + 1, i + 1, p + [arr[i]], cur+arr[i])

arr = [1, 2, 3, 4, 5]
N = len(arr)
R = 3
comb(0, 0, [], 0)