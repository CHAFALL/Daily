import sys
sys.stdin = open('D11879.txt')

# def find_two():
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 2:
#                 return i, j
#
# def maze(i, j):
#     global flag
#     # 방문 체크
#     visited[i][j] = 1
#     if arr[i][j] == 3:
#         flag = 1
#         return
#     for k in range(4):
#         ni = i + di[k]
#         nj = j + dj[k]
#
#         if 0<= ni < N and 0<= nj < N and visited[ni][nj] == 0\
#                 and arr[ni][nj] != 1:
#             maze(ni, nj) # 여기만 내가 실수함
#     return
#
#
# di = [-1, 0, 1, 0]
# dj = [0, -1, 0, 1]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     flag = 0
#
#     si, sj = find_two()
#     maze(si, sj)
#
#     print(flag)
#---------------------------------------------------------------------------------
# 연습

