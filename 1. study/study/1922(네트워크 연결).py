# import heapq
#
# def prim(start):
#     Q = []
#     # 출발점 초기화
#     heapq.heappush(Q, (0, start)) # 가중치, 정점
#     total_w = 0 # 누적합 저장
#     while Q:
#         w, v = heapq.heappop(Q)
#         # 연결 안 되었으면 해주고
#         if not connected[v]:
#             connected[v] = 1
#             total_w += w
#
#         # 갈 수 있는 노드들 체크
#         for nw, nv in adj[v]:
#             if not connected[nv]:
#                 heapq.heappush(Q, (nw, nv))
#
#     return total_w
#
#
# V = int(input())
# E = int(input())
# # 연결 유무 체크
# connected = [0] * (V + 1)
# # 인접리스트 만들기
# adj = [[] for _ in range(V + 1)]
# for _ in range(E):
#     A, B, C = map(int, input().split())
#     adj[A].append((C, B)) # 무향
#     adj[B].append((C, A))
#
#
# print(prim(1))

#----------------------------------------------------------------
def find_set(x):
    if parents[x] == x:
        return x
    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

V = int(input())
E = int(input())
edge = []
parents = [i for i in range(V + 1)]
for _ in range(E):
    A, B, C = map(int, input().split())
    edge.append((C, A, B))

edge.sort()

cnt = 0 # 현재 방문한 정점 수
sum_weight = 0
for w, f, t in edge:
    # 싸이클이 발생하지 않는다면
    # (대표가 같지 않다면?)
    if find_set(f) != find_set(t):
        cnt += 1
        sum_weight += w
        union(f, t)
        # 다 연결되었으면
        if cnt == V:
            break

print(sum_weight)