def dfs(r, c, d):
    global total
    cnt = 0
    while cnt < 3:
        nr = r + dr[d - 1]
        nc = c + dc[d - 1]
        if arr[nr][nc] == 0:
            total += 1
            arr[nr][nc] = 2
            dfs(nr, nc, d)
        cnt += 1
    else:
        # 후진용(뒤로 돌아)
        nd = d - 2
        nr = r + dr[nd]
        nc = c + dc[nd]
        if arr[nr][nc] == 1:
            print(total)
            return
        else:
            dfs(nr, nc, d)


# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]
total = 0
dfs(r, c, d)
