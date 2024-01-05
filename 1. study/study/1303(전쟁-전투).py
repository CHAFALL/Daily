# import sys
# sys.setrecursionlimit(10**6)
# def dfs(i, j, type, number):
#     global W_total, B_total
#     visited[i][j] = 1 # 방문체크
#     for k in range(4):
#         ni = i + di[k]
#         nj = j + dj[k]
#         if 0 <= ni < N and 0 <= nj < M:
#             if visited[ni][nj] == 0 and arr[ni][nj] == type:
#                 dfs(ni, nj, type, number + 1)
#     print(number)
#     # 탐색이 끝났을 때, 빠질 때도 연산이 되어서 크게 나오는 데??
#     if type == 'W':
#         W_total += number**2
#     else:
#         B_total += number**2
#
#
#
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# W_total = 0
# B_total = 0
# N, M = map(int, input().split())
# arr = [list(input()) for _ in range(M)]
# visited = [[0] * N for _ in range(M)]
#
# for i in range(M):
#     for j in range(N):
#         if (arr[i][j] == 'W' or arr[i][j] =='B') and visited[i][j] == 0:
#             dfs(i, j, arr[i][j], 1)
#
# print(W_total)
# print(B_total)
#----------------------------------------------------------------------------------------------------

# import sys
# sys.setrecursionlimit(10**6)
# def dfs(i, j, type):
#     global number
#     visited[i][j] = 1 # 방문체크
#     # 내가 할 일
#     number += 1
#     for k in range(4):
#         ni = i + di[k]
#         nj = j + dj[k]
#         if 0 <= ni < M and 0 <= nj < N:
#             if visited[ni][nj] == 0 and arr[ni][nj] == type:
#                 dfs(ni, nj, type)
#     return
#
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# W_total = 0
# B_total = 0
# N, M = map(int, input().split())
# arr = [list(input()) for _ in range(M)]
# visited = [[0] * N for _ in range(M)]
#
# for i in range(M):
#     for j in range(N):
#         if (arr[i][j] == 'W' or arr[i][j] =='B') and visited[i][j] == 0:
#             number = 0
#             dfs(i, j, arr[i][j])
#             if arr[i][j] == 'W':
#                 W_total += number ** 2
#             elif arr[i][j] == 'B':
#                 B_total += number ** 2
#
# print(W_total, B_total)

#-----------------------------------
import sys
sys.setrecursionlimit(10**6)
def dfs(i, j, type):
    global number
    arr[i][j] = 9 # 방문체크(이렇게 하니깐 밑에서 문제가 발생)
    # 내가 할 일
    number += 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < M and 0 <= nj < N:
            if arr[ni][nj] == type:
                dfs(ni, nj, type)

    return

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
W_total = 0
B_total = 0
N, M = map(int, input().split())
arr = [list(input()) for _ in range(M)]

for i in range(M):
    for j in range(N):
        if (arr[i][j] == 'W' or arr[i][j] =='B'):
            number = 0
            type = arr[i][j] # 따로 저장
            dfs(i, j, type)
            if type == 'W':
                W_total += number ** 2
            elif type == 'B':
                B_total += number ** 2

print(W_total, B_total)
