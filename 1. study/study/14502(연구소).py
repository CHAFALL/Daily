# from collections import deque
# import copy
# def bfs():
#     global total_count
#     # Q 손상 막기
#     arr_copy = copy.deepcopy(arr)
#
#     # 시간 단축을 위해 미리 계산
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 2:
#                 Q.append((i, j))
#
#     while Q:
#         i, j = Q.popleft()
#
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#
#             if 0 <= ni < N and 0 <= nj < M:
#                 if arr_copy[ni][nj] == 0:
#                     arr_copy[ni][nj] = 2
#                     Q.append((ni, nj))
#
#     count = 0
#     for p in range(N):
#         for q in range(M):
#             if arr_copy[p][q] == 0:
#                 count += 1
#
#     total_count = max(total_count, count)
#
#
#
# def make_wall(cnt):
#     if cnt == 3:
#         bfs()
#         return
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 0:
#                 arr[i][j] = 1
#                 make_wall(cnt + 1)
#                 # 원상복구 작업
#                 arr[i][j] = 0
#
#
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
#
# Q = deque()
#
# # # 시간 단축을 위해 미리 계산
# # for i in range(N):
# #     for j in range(M):
# #         if arr[i][j] == 2:
# #            Q.append((i, j))
#
# total_count = 0
#
# make_wall(0)
#
# print(total_count)
#


#----------------------------------------------
from collections import deque
import copy
def bfs():
    global total_count
    # Q 손상 막기
    Q_copy = copy.deepcopy(Q)
    arr_copy = copy.deepcopy(arr)

    while Q_copy:
        i, j = Q_copy.popleft()

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < M:
                if arr_copy[ni][nj] == 0:
                    arr_copy[ni][nj] = 2
                    Q_copy.append((ni, nj))


    # 안전구역 세기
    count = 0
    for p in range(N):
        for q in range(M):
            if arr_copy[p][q] == 0:
                count += 1

    total_count = max(total_count, count)



def make_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                make_wall(cnt + 1)
                # 원상복구 작업
                arr[i][j] = 0


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


Q = deque()

# 시간 단축을 위해 미리 계산
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
           Q.append((i, j))

total_count = 0

make_wall(0)

print(total_count)