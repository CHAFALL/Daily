# def dfs(r, c, d):
#     global total
#     cnt = 0
#     while cnt < 3:
#         nr = r + dr[d - 1]
#         nc = c + dc[d - 1]
#         if arr[nr][nc] == 0:
#             total += 1
#             arr[nr][nc] = 2
#             dfs(nr, nc, d)
#         cnt += 1
#     else:
#         # 후진용(뒤로 돌아)
#         nd = d - 2
#         nr = r + dr[nd]
#         nc = c + dc[nd]
#         if arr[nr][nc] == 1:
#             print(total)
#             return
#         else:
#             dfs(nr, nc, d)
#
#
# # 북, 동, 남, 서
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
# N, M = map(int, input().split())
# r, c, d = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# # visited = [[0] * M for _ in range(N)]
# total = 0
# dfs(r, c, d)
#-------------------------------------------------------
# def dfs(r, c, d):
#     global total
#     if arr[r][c] == 0:
#         total += 1
#     while True:
#         cnt = 0
#         while cnt < 3:
#             # d가 변동이 없구나 이러니깐
#             nr = r + dr[(d + 3) % 4]
#             nc = c + dc[(d + 3) % 4]
#             if arr[nr][nc] == 0:
#                 total += 1
#                 arr[nr][nc] = 2  # 청소 표시
#                 r = nr
#                 c = nc
#                 cnt = 0
#             cnt += 1
#         else:
#             # 후진용(뒤로 돌아)
#             nd = (d + 2) % 4
#             nr = r + dr[nd]
#             nc = c + dc[nd]
#             if arr[nr][nc] == 1:
#                 print(total)
#                 return
#             else:
#                 r = nr
#                 c = nc
#
#
# # 북, 동, 남, 서
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
# N, M = map(int, input().split())
# r, c, d = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# total = 0
# dfs(r, c, d)
#----------------------------------------------------
def dfs(r, c, d):
    total = 0
    if arr[r][c] == 0:
        total += 1
        arr[r][c] = 2
    while True:
        cnt = 0
        while cnt < 3:
            d = (d + 3) % 4
            nr = r + dr[d]
            nc = c + dc[d]
            if arr[nr][nc] == 0:
                total += 1
                arr[nr][nc] = 2  # 청소 표시
                r = nr
                c = nc
                cnt = -1
            cnt += 1

        else:
            # 후진용(뒤로 돌아)
            nd = (d + 2) % 4
            nr = r + dr[nd]
            nc = c + dc[nd]
            if arr[nr][nc] == 1:
                print(total)
                return
            else:
                r = nr
                c = nc


# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dfs(r, c, d)

#------------------------------------------------------
# import sys
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# r, c, d = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# # d => 0,3,2,1 순서로 돌아야한다.
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# # 처음 시작하는 곳 청소
# arr[r][c] = 2
# cnt = 1
#
# while 1:
#     flag = 0
#     # 4방향 확인
#     for _ in range(4):
#         # 0,3,2,1 순서 만들어주기위한 식
#         nx = r + dx[(d + 3) % 4]
#         ny = c + dy[(d + 3) % 4]
#         # 한번 돌았으면 그 방향으로 작업시작
#         d = (d + 3) % 4
#         if arr[nx][ny] == 0:
#             arr[nx][ny] = 2
#             cnt += 1
#             r = nx
#             c = ny
#             # 청소 한 방향이라도 했으면 다음으로 넘어감
#             flag = 1
#             break
#     if flag == 0:  # 4방향 모두 청소가 되어 있을 때,
#         if arr[r - dx[d]][c - dy[d]] == 1:  # 후진했는데 벽
#             print(cnt)
#             break
#         else:
#             r, c = r - dx[d], c - dy[d]
