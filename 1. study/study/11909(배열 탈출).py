# 다익스트라로는 시간초과가 난다구???

import heapq
import sys
input = sys.stdin.readline

def dijkstra(si, sj):
    Q = []
    # 출발점 초기화
    heapq.heappush(Q, (0, si, sj))  # 가중치, 좌표
    D[si][sj] = 0

    while Q:
        w, i, j = heapq.heappop(Q)

        # 이미 더 적은 가중치로 방문한 적이 있다면 pass
        if D[i][j] < w:
            continue

        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                cost = 0
                # 가려는 곳의 높이가 현재 위치보다 높거나 같으면 비용 발생
                if arr[ni][nj] >= arr[i][j]:
                    cost = arr[ni][nj] - arr[i][j] + 1

                if D[ni][nj] > D[i][j] + cost:
                    D[ni][nj] = D[i][j] + cost
                    heapq.heappush(Q, (D[ni][nj], ni, nj))
    return


di = [0, 1]
dj = [1, 0]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
INF = 987654321
D = [[INF] * N for _ in range(N)]
dijkstra(0, 0)

print(D[N-1][N-1])

