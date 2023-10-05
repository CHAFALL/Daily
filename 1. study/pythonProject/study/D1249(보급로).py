def dijkstra(i, j):
    # 시작점 설정
    D[i][j] = 0

    for _ in range(N * N):
        # 가중치 최소값 찾기
        min_v = 987654321
        for i in range(N):
            for j in range(N):
                if min_v > D[i][j] and visited[i][j] == 0:
                    min_v = D[i][j]
                    # 작은 놈 찾고
                    vi, vj = i, j
        # 방문체크
        visited[vi][vj] = 1

        for k in range(4):
            ni = vi + di[k]
            nj = vj + dj[k]

            if 0 <= ni < N and 0 <= nj < N\
                    and not visited[ni][nj]:
                if D[ni][nj] > D[vi][vj] + arr[ni][nj]:
                    D[ni][nj] = D[vi][vj] + arr[ni][nj]
    return


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    D = [[987654321] * N for _ in range(N)]

    dijkstra(0, 0)
    print(f'#{tc} {D[N - 1][N - 1]}')

#----------------------------------------------------------
import heapq

def dijkstra(i, j):
    # 시작점 설정
    D[i][j] = 0

    pq = []
    heapq.heappush(pq, (0, i, j))

    while pq:
        d, vi, vj = heapq.heappop(pq)
        # 방문체크
        visited[vi][vj] = 1

        for k in range(4):
            ni = vi + di[k]
            nj = vj + dj[k]

            if 0 <= ni < N and 0 <= nj < N\
                    and not visited[ni][nj]:
                if D[ni][nj] > D[vi][vj] + arr[ni][nj]:
                    D[ni][nj] = D[vi][vj] + arr[ni][nj]
                    heapq.heappush(pq, (D[ni][nj], ni, nj))
    return


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    D = [[987654321] * N for _ in range(N)]

    dijkstra(0, 0)
    print(f'#{tc} {D[N - 1][N - 1]}')