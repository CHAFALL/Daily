import heapq

def prim(start):
    Q = []
    # 출발점 초기화
    heapq.heappush(Q, (0, start)) # 가중치, 정점
    total_w = 0 # 누적합 저장

    while Q:
        w, v = heapq.heappop(Q)

        if connected[v] == 0:
            connected[v] = 1

        total_w += w
        for

N = int(input())
# 인접 행렬
adj = [list(map(int, input().split())) for _ in range(N)]
connected = [0] * N
prim(0)




#-------------------------------------------------------------
import heapq

def prim(start):
    heap = []
    # MST에 포함되었는 지 여부
    MST = [0] * V

    # 가중치, 정점 정보
    heapq.heappush(heap, (0, start))
    # 누적합 저장
    sum_weight = 0

    # Tip: 디버깅할때 방문 순서로 하기
    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼냄
        weight, v = heapq.heappop(heap)
        # 시작점 체크는 꺼낼 때 할 것임..
        # 이미 방문한 노드라면 pass

        if MST[v]:
            continue
        # 방문 체크
        MST[v] = 1

        # 누적합 추가
        sum_weight += weight
        # 갈 수 있는 노드들을 체크
        for next in range(V):
            # 갈 수 없거나 이미 방문했다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue
            # 가중치, 해당 정점
            heapq.heappush(heap, (graph[v][next], next))

    return sum_weight

V, E = map(int, input().split())
# 인접행렬
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    # from to 가중치
    f, t, w = map(int, input().split())
    graph[f][t] = w
    graph[t][f] = w # 무방향

result = prim(0)
print(f'최소 비용 = {result}')