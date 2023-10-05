import sys
sys.stdin = open('D11780.txt')


# def dfs(v):
#     visited[v] = 1  # 방문체크
#     for w in range(1, V + 1):
#         if visited[w] == 0 and adj[v][w] == 1:
#             dfs(w)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())
#     temp = list(map(int, input().split()))
#     visited = [0] * (V + 1)
#     adj = [[0] * (V + 1) for _ in range(V + 1)]
#     for i in range(E):
#         s, e = temp[2 * i], temp[2 * i + 1]
#         adj[s][e] = adj[e][s] = 1
#     cnt = 0
#     for i in range(1, V + 1):
#         if visited[i] == 0:
#             dfs(i)
#             cnt += 1
#     print(f'#{tc} {cnt}')

#----------------------------------------------------
# 인접 리스트 연습하기
# def dfs(v):
#     visited[v] = 1  # 방문체크
#     for w in adj[v]:
#         if visited[w] == 0:
#             dfs(w)
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     temp = list(map(int, input().split()))
#     visited = [0] * (V + 1)
#     adj = [[] for _ in range(V + 1)]
#
#     for i in range(E):
#         s, e = temp[2 * i], temp[2 * i + 1]
#         adj[s].append(e)
#         adj[e].append(s) # 무향
#
#     cnt = 0
#     for i in range(1, V + 1):
#         if visited[i] == 0:
#             dfs(i)
#             cnt += 1
#     print(f'#{tc} {cnt}')
#------------------------------------------------------------------
# 인접 리스트 이면서 bfs도 연습하기
# def bfs(v):
#     Q = [v]
#     visited[v] = 1  # 방문체크
#
#     while Q:
#         v = Q.pop(0)
#         for w in adj[v]:
#             if visited[w] == 0:
#                 Q.append(w)
#                 visited[w] = 1
#
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())
#     temp = list(map(int, input().split()))
#     visited = [0] * (V + 1)
#     adj = [[] for _ in range(V + 1)]
#
#     for i in range(E):
#         s, e = temp[2 * i], temp[2 * i + 1]
#         adj[s].append(e)
#         adj[e].append(s)  # 무향
#
#     cnt = 0
#     for i in range(1, V + 1):
#         if visited[i] == 0:
#             bfs(i)
#             cnt += 1
#     print(f'#{tc} {cnt}')
#----------------------------------------------------------------
# 교수님 풀이
# "내 부모가 나야"를 카운트 해주면 된다.
def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 정점, 간선
    tmp = list(map(int, input().split()))
    parent = [i for i in range(N + 1)]  # make-set

    for i in range(M):
        s, e = tmp[2 * i], tmp[2 * i + 1]
        # union
        parent[find_set(e)] = find_set(s)

    cnt = 0
    for i in range(1, N+1):
        if parent[i] == i:
            cnt += 1
    print(f'#{tc} {cnt}')