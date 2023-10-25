# 힙 연습
# 최소힙
# import heapq
# heap = []
# heapq.heappush(heap, 3)
# heapq.heappush(heap, 1)
# heapq.heappush(heap, 2)
#
# print(heapq.heappop(heap)) #1
# print(heapq.heappop(heap)) #2
# print(heapq.heappop(heap)) #3

# 최대힙
# import heapq
# heap = []
# heapq.heappush(heap, -3)
# heapq.heappush(heap, -1)
# heapq.heappush(heap, -2)
#
# print(-heapq.heappop(heap)) #3
# print(-heapq.heappop(heap)) #2
# print(-heapq.heappop(heap)) #1

# # 튜플도 될까?
# import heapq
# heap = []
# heapq.heappush(heap, (-3, 2))
# heapq.heappush(heap, (-1, 1))
# heapq.heappush(heap, (-2, 3))
# # 맨앞 기준으로 나온다.
# print(heapq.heappop(heap)) #(-3, 2)
# print(heapq.heappop(heap)) #(-2, 3)
# print(heapq.heappop(heap)) #(-1, 1)

#------------------------------------------------------------------------------

# prim 알고리즘
'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''


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

#-----------------------------------------------------------------------
# Kruskal 알고리즘
#
# '''
# 7 11
# 0 1 32
# 0 2 31
# 0 5 60
# 0 6 51
# 1 2 21
# 2 4 46
# 2 6 25
# 3 4 34
# 3 5 18
# 4 5 40
# 4 6 51
# '''
# # 모든 간선들 중 비용이 가장 적은 걸 우선으로 고르자
# # 이번엔 heapq말고 sort로 해보겠다.
#
V, E = map(int, input().split())
edge = []
for _ in range(E):
    f, t, w = map(int, input().split())

    # 위의 것은 도착지점과 가중치만 있어도 되었는데 이번에는 출발지점도 있어야 됨
    # 어디서 출발하고 도착할 지 모르므로
    edge.append([f, t, w])
# w 를 기준으로 정렬
edge.sort(key=lambda x: x[2])

# 싸이클 고려해야 됨
# 싸이클 발생 여부를 union find로 해결

parents = [i for i in range(V)]

def find_set(x):
    if parents[x] == x:
        return x
    # 경로 압축도 해줌
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        # print('사이클 발생')
        return
    # else 생략한 것임
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


# 현재 방문한 정점 수
cnt = 0
sum_weight = 0
for f, t, w in edge:
    # 싸이클이 발생하지 않는다면
    # (대표가 같지 않다면?)
    if find_set(f) != find_set(t):
        cnt += 1 # 디버깅때 여기 찍고 해보기(그림을 다 그려놓고)(이 알고리즘을 잘 구현했을 때만 여기에 들어오는지 check)
        sum_weight += w
        union(f, t)
        # MST 구성이 끝나면
        if cnt == V:
            break
print(f'최소 비용 = {sum_weight}')
#---------------------------------------------------------------
# Dijkstra
# prim과 서로 다른 사람이 풀어서 그렇지 원래 굉장히 비슷
# 최소값, 선택, 갱신
# 업데이트 방식만 다름
# 즉 인접행렬, 가중치, 방문체크! 필요!!
# 모든 경로를 다 거치는 것이 아닌 최단 경로로
'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''
# 최단 거리 문제 유형
# 1.특정 지점-> 도착 지점까지의 최단 거리: 다익스트라
# 2.가중치에 음수 포함? : 다익스트라 불가(가능하긴 함, 개조하면), 밸만포드
# 3. 여러 지점 -> 여러 지점까지의 최단 거리: 플로이드 - 워샬
#            - 여러 지점 모두 다익스트라 돌리기 -> 시간 복잡도 계산 잘해야 함

# 내가 갈 수 있는 경로 중 누적거리가 제일 짧은 것부터 고르자!
import heapq
# 입력
n, m = map(int, input().split())
# 인접리스트
graph = [[] for i in range(n)]
for _ in range(m):
    f, t, w = map(int, input().split())
    graph[f].append([t, w])

# 1. 누적 거리를 계속 저장
INF = int(1e9) # 최대값으로 1억- 대충 엄청 큰 수, 도달 못하면 이걸 가짐
distance = [INF] * n


def dijkstra(start):
    # 2. 우선순위 큐
    pq = []
    # 출발점 초기화
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        # 현재 시점에서
        # 누적 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)
        # 이미 방문한 지점 + 누적 거리가 더 짧게 방문한 적이 있다면 pass
        if distance[now] < dist:
            continue

        # 인접 노드를 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # next_node로 가기 위한 누적 거리
            new_cost = dist + cost

            # 누적 거리가 기존보다 크네?
            if distance[next_node] <= new_cost:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))
dijkstra(0)
print(distance)