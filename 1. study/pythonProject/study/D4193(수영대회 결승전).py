import sys
sys.stdin = open('D4193.txt')
# from collections import deque
# # 느낌이 BFS 문제인듯
#
# def bfs(i, j, t):
#     Q = deque([(i, j, t)])
#     visited[i][j] = 1 # 방문체크
#     while Q:
#         i, j, t = Q.popleft()
#         # 내가 하고 싶은 일
#         if i == ei and j == ej:
#             return visited[i][j] - 1
#         for k in range(5):
#             ni = i+di[k]
#             nj = j+dj[k]
#             # 이렇게 하면 제자리에 있는 건 우얌?
#             if 0<= ni < N and 0<= nj < N and\
#                 visited[ni][nj] == 0:
#                 if arr[ni][nj] == 0:
#                     Q.append((ni, nj, t+1))
#                     visited[ni][nj] = visited[i][j] + 1
#                 elif arr[ni][nj] == 2:
#                     if t % 3 == 2:
#                         Q.append((ni, nj, t+1))
#                         visited[ni][nj] = visited[i][j] + 1
#
#
#
# # 제자리, 우, 하, 좌, 상
# di = [0, 0, 1, 0, -1]
# dj = [0, 1, 0, -1, 0]
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # 0:지날 수 o, 1:장애물, 2:주기가 2초인 소용돌이
#     si, sj = map(int, input().split())
#     ei, ej = map(int, input().split())
#     visited = [[0] * N for _ in range(N)]
#     # 건널 수 있는 시간대는 t%3 == 2일때 가능
#     print(bfs(si, sj, 0))
#----------------------------------------------------------------
# from collections import deque
# def bfs(i, j, t):
#     Q = deque([(i, j, t)])
#     visited[i][j] = 1 # 방문체크
#     while Q:
#         i, j, t = Q.popleft()
#         # 내가 하고 싶은 일
#         if i == ei and j == ej:
#             return visited[i][j] - 1
#         for k in range(4):
#             ni = i+di[k]
#             nj = j+dj[k]
#
#             if 0<= ni < N and 0<= nj < N and\
#                 visited[ni][nj] == 0:
#                 if arr[ni][nj] == 0:
#                     Q.append((ni, nj, t+1))
#                     visited[ni][nj] = visited[i][j] + 1
#                 # 소용돌이를 만났을 때는 기다리는 형식으로
#                 # (돌아가는 것보다는 기다리는 것이 효율이 높다)
#                 elif arr[ni][nj] == 2:
#                     if t % 3 != 2:
#                         c = 0 # 기다리는 시간
#                         while t % 3 != 2:
#                             t += 1
#                             c += 1
#                         Q.append((ni, nj, t + 1))
#                         visited[ni][nj] = visited[i][j] + c + 1
#                     else:
#                         Q.append((ni, nj, t + 1))
#                         visited[ni][nj] = visited[i][j] + 1
#
#
#
# # 우, 하, 좌, 상
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # 0:지날 수 o, 1:장애물, 2:주기가 2초인 소용돌이
#     si, sj = map(int, input().split())
#     ei, ej = map(int, input().split())
#     visited = [[0] * N for _ in range(N)]
#     # 건널 수 있는 시간대는 t%3 == 2일때 가능
#     print(bfs(si, sj, 0))
#

#---------------------------------------------------------------------------------------------
# from collections import deque
#
# directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#
# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     board = []
#     for _ in range(N):
#         board.append(list(map(int, input().split())))
#     visited = [[False for _ in range(N)] for _ in range(N)]
#     answer = N ** 2
#     A, B = map(int, input().split())
#     C, D = map(int, input().split())
#
#     dq = deque([(A, B, 0)])
#     while dq:
#         y, x, now = dq.popleft()
#         visited[y][x] = True
#         if (y, x) == (C, D):
#             answer = min(answer, now)
#             continue
#         for dy, dx in directions:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < N and 0 <= ny < N:
#                 if board[ny][nx] == 1:
#                     continue
#                 if not visited[ny][nx]:
#                     next_time = now
#                     if board[ny][nx] == 2 and (now - 2) % 3 != 0:
#                         while (next_time - 2) % 3 != 0:
#                             next_time += 1
#                     dq.append((ny, nx, next_time + 1))
#
#     if answer == N ** 2:
#         answer = -1
#     print("#%d %d" % (t, answer))
#-----------------------------------------------------------------
# from collections import deque;
#
#
# # 너비우선 탐색 시작지점, 끝지점의 row, col을 인자로 받는다.
# def bfs(sr, sc, er, ec):  # start end row col : sr sc er ec
#     # deque 생성
#     Q = deque()
#
#     # 시작지점과 시간 0 을 넣는다.
#     Q.append([sr, sc, 0])
#
#     # Q안에 값이 있으면 반복
#     while Q:
#         # Q 맨 앞에 있는 값을 꺼낸다.
#         tmp = Q.popleft()
#         # 목표지점에 도착했다면 걸렸던 시간을 반환
#         if tmp[0] == er and tmp[1] == ec:
#             return tmp[2]
#
#         # 4방향 탐색
#         for d in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
#             # 움직이게 될 row col
#             dr = tmp[0] + d[0]
#             dc = tmp[1] + d[1]
#             # dr dc가 수영 범위 안에 있고 방문한 적이 없다면?
#             if 0 <= dr < N and 0 <= dc < N and not vstd[dr][dc]:
#                 # 섬 장애물이 없는 지역이라면?
#                 if arr[dr][dc] != 1:
#                     # 소용돌이 장애물이 생성되는 지역이라면?
#                     if arr[dr][dc] == 2:
#                         # 지금 소용돌이가 있다면(1초 기다린다.)
#                         if ((tmp[2] + 1) % 3) != 0:
#                             Q.append([tmp[0], tmp[1], tmp[2] + 1])
#                             continue
#                         # 소용돌이가 없거나 장애물이 없는 지역이라면 이동
#                     Q.append([dr, dc, tmp[2] + 1])
#
#             # 모든 이동 가능한 곳을 거치고도 도착하지 못했으면 -1 반환
#     return -1
#
#
# T = int(input())
# for t in range(1, T + 1):
#     # 수영장 크기
#     N = int(input())
#
#     # 수영장 입력받기
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     # 수영장이랑 똑같은 크기의 배열 visited
#     vstd = [[0] * N for _ in range(N)]
#
# # 시작지점 입력받기 start row col
# sr, sc = map(int, input().split())
# # 골인지점 입력받기 end row col
# er, ec = map(int, input().split())
#
# # ans=도착지점까지 걸린시간 bfs()에 시작,목표지점을 넣는다.
# ans = bfs(sr, sc, er, ec)
#
# # 걸린 시간을 출력
# print(f'#{t} {ans}')

#-------------------------------------------------------------
from collections import deque
def bfs(i, j, t):
    Q = deque([(i, j, t)])
    visited[i][j] = 1 # 방문체크
    while Q:
        i, j, t = Q.popleft()
        # 내가 하고 싶은 일
        if i == ei and j == ej:
            return t
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]

            if 0<= ni < N and 0<= nj < N and\
                visited[ni][nj] == 0:

                if arr[ni][nj] == 0:
                    Q.append((ni, nj, t+1))
                    visited[ni][nj] = 1

                elif arr[ni][nj] == 2:
                    # 소용돌이가 있으면 제자리에서 기다리기
                    if t % 3 != 2:
                        Q.append((i, j, t + 1))
                    else:
                        Q.append((ni, nj, t + 1))
                        visited[ni][nj] = 1



# 우, 하, 좌, 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 0:지날 수 o, 1:장애물, 2:주기가 2초인 소용돌이
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())
    visited = [[0] * N for _ in range(N)]
    # 건널 수 있는 시간대는 t%3 == 2일때 가능
    print(f'#{tc} {bfs(si, sj, 0)}')
