import sys
sys.stdin = open('D7465.txt')

def bfs(v):
    Q = [v]
    visited[v] = 1
    while Q:
        v = Q.pop(0)
        for w in adj[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)

    # 인접리스트 만들기
    for _ in range(M):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    cnt = 0
    for i in range(1, N + 1):
        if visited[i] == 0:
            bfs(i)
            cnt += 1
    print(f'#{tc} {cnt}')

#-------------------------------------------------------------------
# "내 부모가 나야"를 카운트 해주면 된다.
def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 정점, 간선
    parent = [i for i in range(N + 1)]  # make-set

    for _ in range(M):
        s, e = map(int, input().split())
        # union
        parent[find_set(e)] = find_set(s)

    cnt = 0
    for i in range(1, N+1):
        if parent[i] == i:
            cnt += 1
    print(f'#{tc} {cnt}')