import heapq

def prim(start):
    Q = []
    # 출발점 초기화
    heapq.heappush(Q, (0, start)) # 가중치, 정점
    D[start] = 0

    while Q:
        w, v = heapq.heappop(Q)
        for n


V, E = map(int, input().split())
visited = [0] * (V + 1)
# 인접리스트 만들기
adj = [[] for _ in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    adj[A].append((C, B)) # (가중치, 도착지)

INF = 2_222_222_222
D = [INF] * (V + 1)
prim(1)



#-----------------------------------------------------------------------
def prim(s):
    total = 0
    # 시작점 설정
    D[s] = 0
    # 정점의 갯수만큼 선택하기
    for i in range(V+1):

        # 가중치 최소값 찾기
        min_v = 987654321
        for j in range(V+1):
            if visited[j] == 0 and D[j] < min_v:
                min_v = D[j]
                v = j # 정점 선택
        # 방문처리(선택)
        visited[v] = 1
        total += adj[PI[v]][v]
        for w in range(V + 1):
            if adj[v][w] and not visited[w]:
                if D[w] > adj[v][w]:
                    D[w] = adj[v][w]
                    PI[w] = v
    return total
# 노드 0부터 시작함
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V + 1)]
    visited = [0] * (V + 1)
    D = [987654321] * (V + 1) # 가중치
    PI = list(range(V + 1)) # 부모

    # 인접행렬
    for _ in range(E):
        # 양 끝 노드 ,가중치
        s, e, w = map(int, input().split())
        adj[s][e] = adj[e][s] = w # 무향

    # 간선의 가중치 합
    print(f'#{tc} {prim(0)}')