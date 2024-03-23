# 낮은 숫자가 큰 숫자를 만나면 갱신하도록
# 다만 같은 초일 때만.
# 바이러스를 que에 넣어서 한 방에 터트리기
# 튜플 필요없고 그냥 작은 숫자를 앞에가도록 처음에 넣고 퍼트리면 끝
from collections import deque


# def bfs():
#     temp = [] # 바이러스 종류, 바이러스 위치
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] != 0:
#                 temp.append((arr[i][j], 0, i, j))
#     # 번호 빠른 놈들이 먼저 자리 차지
#     temp.sort()
#     Q = deque(temp)
#     while Q:
#         v, time, r, c = Q.popleft()
#         # 할 일
#         arr[r][c] = v
#         if time == S:
#             return
#         for k in range(4):
#             nr = r + dr[k]
#             nc = c + dc[k]
#             if 0 <= nr < N and 0 <= nc < N:
#                 if arr[nr][nc] == 0:
#                     Q.append((v, time + 1, nr, nc))
#
#     return
#
#
#
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
# N, K = map(int, input().split())  # K: 바이러스 번호
# arr = [list(map(int, input().split())) for _ in range(N)]
# S, X, Y = map(int, input().split())
#
# bfs()
# print(arr[X-1][Y-1])


# from collections import deque
#
# def bfs():
#     temp = [] # 바이러스 종류, 바이러스 위치
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] != 0:
#                 temp.append((arr[i][j], i, j))
#     # 번호 빠른 놈들이 먼저 자리 차지
#     temp.sort()
#     Q = deque(temp)
#     while Q:
#         v, r, c = Q.popleft()
#         for k in range(4):
#             nr = r + dr[k]
#             nc = c + dc[k]
#             if 0 <= nr < N and 0 <= nc < N:
#                 if arr[nr][nc] == 0:
#                     visited[nr][nc] = visited[r][c] + 1
#                     arr[nr][nc] = v
#                     Q.append((v, nr, nc))
#
#     return
#
#
#
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
# N, K = map(int, input().split())  # K: 바이러스 번호
# arr = [list(map(int, input().split())) for _ in range(N)]
# S, X, Y = map(int, input().split())
# visited = [[0] * N for _ in range(N)]
#
# bfs()
#
# if visited[X-1][Y-1] > S:
#     print(0)
# else:
#     print(arr[X-1][Y-1])
#

#---------------------------------------------------------
import heapq

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, K = map(int, input().split())  # K: 바이러스 번호
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
visited = [[0] * N for _ in range(N)]

Q = []
for r in range(N):
    for c in range(N):
        if arr[r][c]:
            heapq.heappush(Q, (arr[r][c], r, c))

while Q:
    v, r, c = heapq.heappop(Q)
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == 0:
                visited[nr][nc] = visited[r][c] + 1
                arr[nr][nc] = v
                heapq.heappush(Q, (arr[nr][nc], nr, nc))

    break

if visited[X-1][Y-1] > S:
    print(0)
else:
    print(arr[X-1][Y-1])


import heapq

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, K = map(int, input().split())  # K: 바이러스 번호
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

Q = []
for r in range(N):
    for c in range(N):
        if arr[r][c]:
            heapq.heappush(Q, (0, arr[r][c], r, c))

while Q:
    sec, v, r, c = heapq.heappop(Q)
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            if arr[nr][nc] == 0 and sec < S:
                arr[nr][nc] = v
                heapq.heappush(Q, (sec + 1, arr[nr][nc], nr, nc))


print(arr[X-1][Y-1])

