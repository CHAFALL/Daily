from collections import deque
def bfs():
    # 모두 익었을 때의 수 = 전체 - 토마토가 들어있지 않는 칸
    total = N * M # 전체 초기값
    cnt = 0
    Q = deque()
    for si in range(M):
        for sj in range(N):
            # 토마토가 들어있지 않다면 전체에서 빼주기
            if arr[si][sj] == -1:
                total -= 1
            # 토마토가 있다면 익은 토마토 카운트
            if arr[si][sj] == 1:
                Q.append((si, sj))
                visited[si][sj] = 1
                cnt += 1
    while Q:
        i, j = Q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < M and 0 <= nj < N:
                if arr[ni][nj] == 0 and not visited[ni][nj]:
                    Q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
										# 익으면서 카운트
                    cnt += 1
    # 모두 익은 경우
    if total == cnt:
        return visited[i][j] - 1
    else:
        return -1

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]


print(bfs())
