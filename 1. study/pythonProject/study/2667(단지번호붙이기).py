from collections import deque
def bfs(si, sj):
    cnt = 1
    visited[si][sj] = 1 # 방문체크
    Q = deque()
    Q.append((si, sj))

    while Q:
        i, j = Q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if arr[ni][nj] == 1:
                    Q.append((ni, nj))
                    visited[ni][nj] = 1
                    cnt += 1
    return cnt


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N = int(input())
visited = [[0] * N for _ in range(N)]
arr = [list(map(int, input())) for _ in range(N)]

ans_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            ans_list.append(bfs(i, j))

ans_list.sort() # 오름차순
M = len(ans_list)

print(M)
for i in range(M):
    print(ans_list[i])


