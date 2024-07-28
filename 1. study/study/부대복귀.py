# 시간 초과
# from collections import deque
#
# def bfs(n, adj, destination, src):
#
#     visited = [-1] * (n + 1)
#     # 초기 설정
#     visited[src] = 0
#     Q = deque([src])
#
#     while Q:
#         v = Q.popleft()
#
#         if v == destination:
#             return visited[v]
#
#         for w in adj[v]:
#             if visited[w] == -1:
#                 visited[w] = visited[v] + 1
#                 Q.append(w)
#
#     return -1
#
#
# def solution(n, roads, sources, destination):
#     adj = [[] for _ in range(n + 1)]
#     # 인접 리스트 만들기
#     for road in roads:
#         s, e = map(int, road)
#         # 양방향 (왕복 가능)
#         adj[s].append(e)
#         adj[e].append(s)
#
#     result = []
#     for src in sources:
#         result.append(bfs(n, adj, destination, src))
#
#     return result
#
# print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))


#--------
from collections import deque

def bfs(n, adj, destination):

    visited = [-1] * (n + 1)
    # 초기 설정
    visited[destination] = 0
    Q = deque([destination])

    while Q:
        v = Q.popleft()

        for w in adj[v]:
            if visited[w] == -1:
                visited[w] = visited[v] + 1
                Q.append(w)

    return visited


def solution(n, roads, sources, destination):
    adj = [[] for _ in range(n + 1)]
    # 인접 리스트 만들기
    for road in roads:
        s, e = map(int, road)
        # 양방향 (왕복 가능)
        adj[s].append(e)
        adj[e].append(s)

    # 목적지에서 출발지로 가자!!!
    result = bfs(n, adj, destination)

    return [result[src] for src in sources]

print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))