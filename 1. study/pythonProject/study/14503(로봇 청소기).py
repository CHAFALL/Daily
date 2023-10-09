import sys
sys.setrecursionlimit(10000)

def dfs(r, c, d, cnt, total):
    visited[r][c] = 1  # 방문체크

    if cnt == 4:
        # 뒤로 돌기
        d = (d-2) % 4
        nr = r + dr[d]
        nc = c + dc[d]
        if arr[nr][nc] == 1 or visited[nr][nc]:
            print(total)
            return
        else:
            dfs(nr, nc, d, 0, total)

    while cnt < 4:
        d = (d-1) % 4
        nr = r + dr[d]
        nc = c + dc[d]
        
        if arr[nr][nc] == 0 and visited[nr][nc] == 0:
            dfs(nr, nc, d, 0, total + 1)
            break
        cnt += 1

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dfs(r, c, d, 0, 1)
#----------------------------------------------------------
# 머리 돌아갈 때 다시 풀기