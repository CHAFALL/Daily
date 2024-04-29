# 프림 문제. heapq 쓰기

import heapq

def prim(n, adj):

    total = 0
    heap = []
    visited = [False] * n
    heapq.heappush(heap, (0, 0))

    while heap:
        w, now = heapq.heappop(heap) # 가중치, 다음으로 볼 연결된 노드
        if visited[now]:
            continue
        visited[now] = True

        # 누적합 추가
        total += w

        for next_w, next in adj[now]:
            if visited[next]:
                continue

            heapq.heappush(heap, (next_w, next))

    return total


def solution(n, costs):


    # 간선의 갯수
    m = len(costs)

    # 연결 시키기 (0부터 시작)
    adj = [[] for _ in range(n)]
    for i in range(m):
        a, b, w = costs[i]
        adj[a].append((w, b))  # 가중치, 어떤 노드랑 연결?
        adj[b].append((w, a))



    return prim(n, adj)


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))


#------
