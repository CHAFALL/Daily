# from collections import deque
#
# # 현재 상어가 노릴 수 있는 최적의 사냥감 찾기
# def bfs(i, j):
#     Q = deque()
#     Q.append((i, j))
#
#     # 방문과 거리 기록도 함수 호출 시 마다 초기화 필요.
#     visited = [[0] * N for _ in range(N)]
#     distance = [[0] * N for _ in range(N)]
#
#     possible_eat = []
#     while Q:
#         i, j = Q.popleft()
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0 <= ni < N and 0 <= nj < N:
#                 if arr[ni][nj] <= sharksize and not visited[ni][nj]:  # 이동이 가능하면
#                     visited[ni][nj] = 1
#                     # 이동할 때마다 거리 1 증가
#                     distance[ni][nj] = distance[i][j] + 1
#                     Q.append((ni, nj))
#                     # 이동하는데 물고기를 만났네?? 근데 먹을 수 있네??
#                     if arr[ni][nj] < sharksize and arr[ni][nj] != 0:
#                         possible_eat.append((distance[ni][nj], ni, nj))
#
#     possible_eat.sort(key=lambda x: (x[0], x[1], x[2])) # 정렬(거리, x, y 순으로)
#     return possible_eat
#
#
# di = [-1, 0, 1, 0]
# dj = [0, -1, 0, 1]
#
# N = int(input())
# # 1, 2, 3, 4, 5, 6 : 물고기 크기, 0: 빈칸, 9: 아기상어 위치
# sharksize = 2
# arr = [list(map(int, input().split())) for _ in range(N)]
#
#
#
# # 상어 위치 가져오기
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 9:
#             arr[i][j] = 0
#             shark_i, shark_j = i, j
#
# # 걸린 시간
# ans = 0
# # 먹은 수
# cnt = 0
#
# while True:
#     fishbin = bfs(shark_i, shark_j)
#
#     if len(fishbin) == 0: # 먹을 수 있는 먹이가 없다면.. 엄마!
#         print(ans)
#         break
#
#     distance, shark_i, shark_j = fishbin[0]
#     # shark_i, shark_j = shark_ni, shark_nj
#     cnt += 1
#     # 상어 크기만큼 먹었다면.
#     if sharksize == cnt:
#         cnt = 0
#         sharksize += 1
#
#     arr[shark_i][shark_j] = 0
#     ans += distance
#----------------------------------------------------------------
from collections import deque

# 현재 상어가 노릴 수 있는 최적의 사냥감 찾기
def bfs(i, j):
    Q = deque()
    Q.append((i, j))

    # 방문 기록도 함수 호출 시 마다 초기화 필요.
    visited = [[0] * N for _ in range(N)]

    possible_eat = []
    while Q:
        i, j = Q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] <= sharksize and not visited[ni][nj]:
                    # 이동할 때마다 거리 1 증가
                    visited[ni][nj] = visited[i][j] + 1
                    Q.append((ni, nj))
                    # 이동하는데 물고기를 만났네?? 근데 먹을 수 있네??
                    if arr[ni][nj] < sharksize and arr[ni][nj] != 0:
                        possible_eat.append((visited[ni][nj], ni, nj))

    possible_eat.sort(key=lambda x: (x[0], x[1], x[2])) # 정렬(거리, x, y 순으로)
    return possible_eat


di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

N = int(input())
# 1, 2, 3, 4, 5, 6 : 물고기 크기, 0: 빈칸, 9: 아기상어 위치
sharksize = 2
arr = [list(map(int, input().split())) for _ in range(N)]



# 상어 위치 가져오기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            arr[i][j] = 0
            shark_i, shark_j = i, j

# 걸린 시간
ans = 0
# 먹은 수
cnt = 0

while True:
    fishbin = bfs(shark_i, shark_j)

    if len(fishbin) == 0: # 먹을 수 있는 먹이가 없다면.. 엄마!
        print(ans)
        break

    distance, shark_i, shark_j = fishbin[0]
    # shark_i, shark_j = shark_ni, shark_nj
    cnt += 1
    # 상어 크기만큼 먹었다면.
    if sharksize == cnt:
        cnt = 0
        sharksize += 1

    arr[shark_i][shark_j] = 0
    ans += distance










