def perm(N, k):
    global max_value
    if k == N:
        # 하고 싶은 일 하기
        total = 0
        for i in range(N - 1):
            total += abs(p[i] - p[i + 1])
        max_value = max(total, max_value)
        return

    for i in range(N):
        if visited[i] == 0: # 방문 안 했으면 방문 체크 해주고
            visited[i] = 1
            p[k] = arr[i]
            perm(N, k+1)
            visited[i] = 0


N = int(input())
arr = list(map(int, input().split()))
visited = [0] * N

p = [0] * N
max_value = -999999
perm(N, 0)
print(max_value)



#----------------------------------------------------

# def perm(k, p):
#     global max_value
#     if k == N:
#         # 하고 싶은 일 하기
#         total = 0
#         for i in range(N-1):
#             total += abs(p[i] - p[i + 1])
#         max_value = max(total, max_value)
#         return
#
#     for i in range(N):
#         if visited[i] == 0:
#             visited[i] = 1
#             perm(k + 1, p + [arr[i]])
#             visited[i] = 0
#
#
# N = int(input())
# arr = list(map(int, input().split()))
# visited = [0] * N
#
# # p = [0] * N
# # perm(N, 0)
# max_value = -999999
# perm(0, [])
# print(max_value)
