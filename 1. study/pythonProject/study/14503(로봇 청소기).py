# import sys
# sys.setrecursionlimit(10000)
#
# def dfs(r, c, d, cnt, total):
#     visited[r][c] = 1  # 방문체크
#
#     if cnt == 4:
#         # 뒤로 돌기
#         nd = (d-2) % 4
#         nr = r + dr[nd]
#         nc = c + dc[nd]
#         if arr[nr][nc] == 1 or visited[nr][nc]:
#             print(total)
#             return
#         else:
#             dfs(nr, nc, d, 0, total)
#
#     while cnt < 4:
#         d = (d-1) % 4
#         nr = r + dr[d]
#         nc = c + dc[d]
#
#         if arr[nr][nc] == 0 and visited[nr][nc] == 0:
#             dfs(nr, nc, d, 0, total + 1)
#             break
#         cnt += 1
#     else:
#         dfs(r, c, d, 0, total)
#
# # 북, 동, 남, 서
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
# N, M = map(int, input().split())
# r, c, d = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]
# dfs(r, c, d, 0, 1)
#----------------------------------------------------------
def dfs(r, c, d):
    global cnt, total
    visited[r][c] = 1 # 방문체크
    # 4방향 모두 청소 할 곳이 없으면 후진
    while True:
        if cnt == 4:
            nd = d - 2
            # 뒤돌기(되돌려줘야 되나?, 후진이니깐)
            nr = r + dr[(nd % 4)]
            nc = c + dr[(nd % 4)]
            # 후진 할 곳이 벽이라면..청소 끝
            if arr[nr][nc] == 1:
                print(total)
                return
            # 아니라면 후진
            else:
                dfs(nr, nc, d)
        while cnt < 4:
            d = (d - 1) % 4
            nr = r + dr[d]
            nc = r + dc[d]
            # 청소해야 할 곳이고 방문한 적이 없다면
            if arr[nr][nc] == 0 and visited[nr][nc] == 0:
                total += 1
                dfs(nr, nc, d)
                break
            cnt += 1


# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
N, M = map(int, input().split())
sr, sc, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt = total = 0
dfs(sr, sc, d)
print(total)