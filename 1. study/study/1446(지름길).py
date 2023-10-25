import heapq

N, D = map(int, input().split())  # D : 고속도로의 길이
# 인접리스트
graph = [[] for _ in range(D + 1)]

for i in range(D):
    graph[i].append((i + 1, 1))  # 도착점, 가중치

for i in range(N):
    s, e, length = map(int, input().split())
    if e <= D:
        graph[s].append((e, length))  # 도착점, 가중치

INF = 987654321
dist = [INF] * (D + 1)

# 초기화
Q = []
heapq.heappush(Q, (0, 0)) # 가중치, 정점
dist[0] = 0

while Q:
    now_dist, now = heapq.heappop(Q)
    # if dist[now] < d: continue

    for next, length in graph[now]:
        cost = now_dist + length

        if dist[next] > cost:
            dist[next] = cost
            heapq.heappush(Q, (dist[next], next))

print(dist[D])
