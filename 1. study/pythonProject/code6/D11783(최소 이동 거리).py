import sys
sys.stdin = open('D11783.txt')
#
# def dijkstra(s):
#     # 시작점 설정
#     D[s] = 0
#     # 정점의 갯수만큼 선택하기
#     for i in range(N + 1): # 인덱스 0번부터 시작
#         # 가중치 최소값 찾기
#         min_v = 987654321
#         for j in range(N + 1):
#             if visited[j] == 0 and min_v > D[j]:
#                 min_v = D[j]
#                 v = j # 너가 젤 작구나 정점 당첨
#
#         # 방문처리(선택)
#         visited[v] = 1
#         # 다음 타겟은 누구??
#         for w in range(N + 1):
#             # 좀 더 효율이 좋은 가중치로 덮어쓰기
#             if adj[v][w] and not visited[w]:
#                 if D[w] > D[v] + adj[v][w]:
#                     D[w] = D[v] + adj[v][w]
#     return
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, E = map(int, input().split())
#     adj = [[0] * (N + 1) for _ in range(N + 1)]
#     visited = [0] * (N + 1)
#     D = [987654321] * (N + 1) # 가중치
#     # 인접행렬 만들기
#     for _ in range(E):
#         s, e, w = map(int, input().split())
#         adj[s][e] = w
#
#     dijkstra(0)
#     print(f'#{tc} {D[-1]}')
#
#---------------------------------------------------------------
# 교수님 풀이
def dijkstra(s):
    # 1. 시작점 설정
    D[s] = 0
    # 2. 정점의 갯수만큼 선택하기
    for _ in range(V):  # 인덱스 0번부터 시작
        # 2.1. 최소값 찾기
        min_v = INF
        for i in range(V):
            if visited[i] == 0 and min_v > D[i]:
                min_v = D[i]
                v = i  # 너가 젤 작구나 정점 당첨

        # 2.2 방문체크(선택)
        visited[v] = 1
        # 여기서 하고 싶은 일을 하면 된다.
        # if v == N:
        #     return D[v]

        # 2.3 다음 타겟은 누구?? (가중치 갱신)
        for w in range(N + 1):
            # (좀 더 효율이 좋은 가중치로 덮어쓰기)
            if adj[v][w] and not visited[w]:
                if D[w] > D[v] + adj[v][w]:
                    D[w] = D[v] + adj[v][w]
    return

INF = 987654321 # 이렇게 하면 아주 약간 빠름
T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    V = N + 1  # 정점의 갯수(0 ~ N)
    adj = [[0] * V for _ in range(V)]  # 인접행렬
    D = [INF] * V  # 가중치 배열
    visited = [0] * V
    # 인접행렬 만들기
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w # 유향

    dijkstra(0)
    print(f'#{tc} {D[N]}')
