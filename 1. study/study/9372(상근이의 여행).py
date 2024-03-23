# def DFS(v):
#     global cnt
#     visited[v] = 1  # 방문체크
#     cnt += 1
#
#     for w in tree[v]:
#         if not visited[w]:
#             DFS(w)
#
#     return
#
# T = int(input())
# for _ in range(1, T+1):
#     N, M = map(int, input().split())
#
#     # 이미 들린 나라를 또 들릴 필요는 없으므로
#     visited = [0] * (N + 1)
#     # 인접리스트
#     tree = [[] for _ in range(N + 1)]
#     for _ in range(M):
#         s, e = map(int, input().split())
#         tree[s].append(e)
#         tree[e].append(s) # 양방향
#
#     cnt = 0
#     DFS(1)
#     print(cnt - 1)


#-----------------------------------------

def DFS(v, cnt):
    visited[v] = 1  # 방문체크


    for w in tree[v]:
        if not visited[w]:
            cnt = DFS(w, cnt + 1)

    return cnt

T = int(input())
for _ in range(1, T+1):
    N, M = map(int, input().split())

    # 이미 들린 나라를 또 들릴 필요는 없으므로
    visited = [0] * (N + 1)
    # 인접리스트
    tree = [[] for _ in range(N + 1)]
    for _ in range(M):
        s, e = map(int, input().split())
        tree[s].append(e)
        tree[e].append(s) # 양방향

    cnt = DFS(1, 0)

    print(cnt)


