import heapq, sys
sys.stdin = open('D11783.txt')


def dijkstra(start):
    # 초기값 설정
    Q = []
    heapq.heappush(Q, (0, start))
    D[start] = 0

    while Q:
        w, v = heapq.heappop(Q)
        for nw, nv in adj[v]:
            cost = w + nw
            if D[nv] > cost:
                D[nv] = cost
                heapq.heappush(Q, (D[nv], nv))

    return

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    # 인접리스트
    adj = [[] for _ in range(N+1)] # 인덱스 0부터 시작
    INF = 987654321
    D = [INF] * (N+1)
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append((w, e))  # 가중치, 도착지점

    dijkstra(0)

    print(D[-1])