import heapq


def dijkstra(S):
    Q = []
    # 출발점 초기화
    heapq.heappush(Q, (0, S))  # 가중치, 정점
    D[S] = 0
    while Q:
        w, v = heapq.heappop(Q)
        for nw, nv in adj[v]:
            cost = w + nw
            # 가중치 갱신(젤 좋은 놈으로)
            if D[nv] > cost:
                D[nv] = cost
                heapq.heappush(Q, (D[nv], nv))
    return


V, E = map(int, input().split())
S = int(input())
adj = [[] for _ in range(V + 1)]
for _ in range(E):
    # s에서 e로 가는 가중치
    s, e, w = map(int, input().split())
    adj[s].append((w, e))

INF = 987654321
D = [INF] * (V + 1)

dijkstra(S)

for i in range(1, V + 1):
    if D[i] == INF:
        print('INF')
    else:
        print(D[i])
