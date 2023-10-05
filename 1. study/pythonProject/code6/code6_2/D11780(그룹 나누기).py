import sys
sys.stdin = open('D11780.txt')
# dfs(인접 행렬)로 풀기
# def dfs(v):
#     # 방문체크
#     visited[v] = 1
#
#     for w in range(1, N + 1):
#         if not visited[w] and adj[v][w] == 1:
#             dfs(w)
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     temp = list(map(int, input().split()))
#     visited = [0] * (N + 1)
#     adj = [[0] * (N + 1) for _ in range(N + 1)]
#
#     # 인접 행렬 만들기
#     for i in range(M):
#         s, e = temp[2 * i], temp[2 * i + 1]
#         adj[s][e] = adj[e][s] = 1 # 무향
#
#     cnt = 0
#     for i in range(1, N + 1):
#         if not visited[i]:
#             cnt += 1
#             dfs(i)
#
#     print(f'#{tc} {cnt}')

#------------------------------------------------------
# bfs(인접 행렬)로 풀기, deq때 하고싶은 일 해봄(방문체크)
# def bfs(v):
#     Q = [v]
#
#     while Q:
#         v = Q.pop(0)
#         visited[v] = 1  # 방문체크
#         for w in range(1, N + 1):
#             if not visited[w] and adj[v][w] == 1:
#                 Q.append(w)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     temp = list(map(int, input().split()))
#     visited = [0] * (N + 1)
#     adj = [[0] * (N + 1) for _ in range(N + 1)]
#
#     # 인접 행렬 만들기
#     for i in range(M):
#         s, e = temp[2 * i], temp[2 * i + 1]
#         adj[s][e] = adj[e][s] = 1  # 무향
#
#     cnt = 0
#     for i in range(1, N + 1):
#         if not visited[i]:
#             cnt += 1
#             bfs(i)
#
#     print(f'#{tc} {cnt}')
#

#----------------------------------
# bfs(인접 행렬)로 풀기, 평소 하던대로
# def bfs(v):
#     Q = [v]
#     visited[v] = 1  # 방문체크
#     while Q:
#         v = Q.pop(0)
#         for w in range(1, N + 1):
#             if not visited[w] and adj[v][w] == 1:
#                 Q.append(w)
#                 visited[w] = visited[v] + 1
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     temp = list(map(int, input().split()))
#     visited = [0] * (N + 1)
#     adj = [[0] * (N + 1) for _ in range(N + 1)]
#
#     # 인접 행렬 만들기
#     for i in range(M):
#         s, e = temp[2 * i], temp[2 * i + 1]
#         adj[s][e] = adj[e][s] = 1  # 무향
#
#     cnt = 0
#     for i in range(1, N + 1):
#         if not visited[i]:
#             cnt += 1
#             bfs(i)
#
#     print(f'#{tc} {cnt}')

#-----------------------------------------------------
# dfs(인접리스트)로 풀기

# def dfs(v):
#     # 방문체크
#     visited[v] = 1
#
#     for w in adj[v]:
#         if not visited[w]:
#             dfs(w)
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     temp = list(map(int, input().split()))
#     visited = [0] * (N + 1)
#     adj = [[] for _ in range(N + 1)]
#
#     # 인접 리스트 만들기
#     for i in range(M):
#         s, e = temp[2 * i], temp[2 * i + 1]
#         adj[s].append(e)
#         adj[e].append(s)  # 무향
#
#     cnt = 0
#     for i in range(1, N + 1):
#         if not visited[i]:
#             cnt += 1
#             dfs(i)
#
#     print(f'#{tc} {cnt}')
#-------------------------------------------------
# bfs(인접리스트)로 풀기

# def bfs(v):
#     Q = [v]
#     visited[v] = 1  # 방문체크
#     while Q:
#         v = Q.pop(0)
#         for w in adj[v]:
#             if not visited[w]:
#                 Q.append(w)
#                 visited[w] = visited[v] + 1
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     temp = list(map(int, input().split()))
#     visited = [0] * (N + 1)
#     adj = [[] for _ in range(N + 1)]
#
#     # 인접 리스트 만들기
#     for i in range(M):
#         s, e = temp[2 * i], temp[2 * i + 1]
#         adj[s].append(e)
#         adj[e].append(s)  # 무향
#
#     cnt = 0
#     for i in range(1, N + 1):
#         if not visited[i]:
#             cnt += 1
#             bfs(i)
#
#     print(f'#{tc} {cnt}')
#---------------------------------------------------
# Union 이용
# '부모가 자기 자신'을 카운트 해주면 된다.
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
    for i in range(1, N + 1):
        if parent[i] == i:
            cnt += 1
    print(f'#{tc} {cnt}')