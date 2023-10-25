def dijkstra(x, y):
    for _ in range(N * N):
        # 최솟값 찾기
        min_v = 999999
        for i in range(N):
            for j in range(N):
                if min_v > D[i][j] and visit[i][j] == 0:
                    min_v = D[i][j]
                    min_i, min_j = i, j

        # 방문 체크
        visit[min_i][min_j] = 1

        # 갱신
        di = [1, -1, 0, 0]
        dj = [0, 0, -1, 1]
        for k in range(4):
            ni = min_i + di[k]
            nj = min_j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if visit[ni][nj] == 0:
                    diff = 0
                    if arr[min_i][min_j] < arr[ni][nj]:
                        diff = arr[ni][nj] - arr[min_i][min_j]
                    if D[ni][nj] > D[min_i][min_j] + diff + 1:
                        D[ni][nj] = D[min_i][min_j] + diff + 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    D = [[9999] * N for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    D[0][0] = 0
    dijkstra(0, 0)
    print(f'#{tc} {D[N - 1][N - 1]}')