# from collections import deque
#
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
#
# N = int(input())
# K = int(input())  # 사과의 개수
#
# arr = [[0] * N for _ in range(N)]
# for _ in range(K):
#     R, C = map(int, input().split())
#     arr[R-1][C-1] = 1  # 사과 위치 넣어주기 # why???
#
#
#
# L = int(input())  # 뱀의 방향 변환 횟수
#
# direct_dict = {}
# for _ in range(L):
#     X, C = input().split() # X 초 후 방향 전환 방향 (L: 왼, D: 오)
#     X = int(X)
#     direct_dict[X] = C  # 딕셔너리에 값 넣기
#
#
# # 뱀의 초기 상태
# snake = deque()
# snake.append((0, 0))
#
# time = 0  # 걸린 시간
# k = 0  # 방향
# while True:
#     r, c = snake[0]
#
#     time += 1
#     nr = r + dr[k]
#     nc = c + dc[k]
#
#     # 종료 조건
#     if nr < 0 or nr >= N or nc < 0 or nc >= N or (nr, nc) in snake:
#         print(time)
#         break
#     # 사과가 있을 때
#     if arr[nr][nc] == 1:
#         arr[nr][nc] = 0 # 냠냠
#         snake.append((nr, nc))
#
#     # 사과가 없을 때
#     elif arr[nr][nc] == 0:
#         snake.append((nr, nc))
#         snake.popleft()
#
#     # 방향 전환 part
#     if time in direct_dict:
#         if direct_dict[time] == 'L':
#             k = (k + 3) % 4
#         elif direct_dict[time] == 'D':
#             k = (k + 1) % 4

#-------------------------------------
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N = int(input())
K = int(input())  # 사과의 개수

arr = [[0] * N for _ in range(N)]
for _ in range(K):
    R, C = map(int, input().split())
    arr[R-1][C-1] = 1  # 사과 위치 넣어주기

L = int(input())  # 뱀의 방향 변환 횟수

direct_dict = {}
for _ in range(L):
    X, C = input().split() # X 초 후 방향 전환 방향 (L: 왼, D: 오)
    X = int(X)
    direct_dict[X] = C  # 딕셔너리에 값 넣기


# 뱀의 초기 상태
snake = deque()
snake.append((0, 0))

time = 0  # 걸린 시간
k = 0  # 방향
while True:
    r, c = snake[-1]

    time += 1
    nr = r + dr[k]
    nc = c + dc[k]

    # 종료 조건(내민 머리가 어디에 닿았으면)
    if nr < 0 or nr >= N or nc < 0 or nc >= N or (nr, nc) in snake:
        print(time)
        break

    # 사과가 있는 없든 머리가 들어간다.
    snake.append((nr, nc))

    # 사과가 있을 때
    if arr[nr][nc] == 1:
        arr[nr][nc] = 0 # 냠냠

    # 사과가 없을 때
    elif arr[nr][nc] == 0:
        snake.popleft()

    # 방향 전환 part
    if time in direct_dict:
        if direct_dict[time] == 'L':
            k = (k + 3) % 4
        elif direct_dict[time] == 'D':
            k = (k + 1) % 4