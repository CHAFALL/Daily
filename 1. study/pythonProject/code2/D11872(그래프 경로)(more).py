import sys
sys.stdin = open('D11872.txt')

# def dfs(v):
#     #방문 체크
#     visited[v] = 1
#     for w in range(1, V+1):
#         if adj[v][w] == 1 and visited[w] == 0:
#             dfs(w)
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     #인접행렬 초기설정
#     adj = [[0] * (V+1) for _ in range(V+1)]
#     # 방문 초기 설정
#     visited = [0] * (V + 1)
#     # 간선 정보를 통해 인접 행렬 만들기
#     for _ in range(E):
#         s, e = map(int, input().split())
#         adj[s][e] = 1
#     # 경로 확인할 출발 노드와 도착 노드
#     S, G = map(int, input().split())
#     dfs(S)
#
#     print(f'#{tc} {visited[G]}')
# ---------------------------------------------------
# 연습
# def dfs(v):
#     visited[v] = 1
#     for w in range(V+1):
#         if visited[w] == 0 and adj[v][w] == 1:
#             dfs(w)
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     # 초기 설정
#     adj = [[0] * (V+1) for _ in range(V+1)]
#     visited = [0] * (V+1)
#     for _ in range(E):
#         s, e = map(int, input().split())
#         adj[s][e] += 1
#
#     S, G = map(int, input().split())
#     dfs(S)
#
#
#     print(visited[G])