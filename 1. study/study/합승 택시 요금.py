import heapq

def dijkstra(n, adj, s, e):
    D = [987654321] * (n + 1)
    # 초기 설정
    Q = [(0, s)]
    D[s] = 0
    while Q:
        cost, now = heapq.heappop(Q)

        if now == e:
            return D[e]

        # 이게 필요한 이유는????
        if D[now] < cost:
            continue
        for next in range(1, n + 1):
            if adj[now][next]:
                next_cost = cost + adj[now][next]
                if D[next] > next_cost:
                    D[next] = next_cost
                    heapq.heappush(Q, (next_cost, next))

    return 987654321

def solution(n, s, a, b, fares):

    # 인접 리스트 만들기
    adj = [[0] * (n + 1) for _ in range(n + 1)]
    for fare in fares:
        start, end, cost = fare
        adj[start][end] = cost
        adj[end][start] = cost

    ans = 987654321

    for i in range(1, n + 1):
        ans = min(ans, dijkstra(n, adj, s, i) + dijkstra(n, adj, i, a) + dijkstra(n, adj, i, b))

    return ans

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))


# A에 대해서 최단 경로를 찾고 visited = 1로 해주고
# B에 대해서 최단 경로 찾을 때는 visited = 1이면 값을 안 더하고 2이면??
# 근데 이렇게 하면 타이밍이 어긋날 때 에러가 날듯