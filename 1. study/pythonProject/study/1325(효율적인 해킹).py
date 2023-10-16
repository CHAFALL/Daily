from collections import deque

def bfs(v):
    cnt = 0
    Q = deque()
    Q.append(v)
    visited[v] = 1

    while Q:
        v = Q.popleft()
        for w in adj[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                Q.append(w)
                cnt += 1
    return cnt


N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    e, s = map(int, input().split())
    adj[s].append(e)

ans_list = []
for i in range(1, N + 1):
    visited = [0] * (N + 1)
    ans_list.append(bfs(i))

max_v = max(ans_list)
for i in range(N):
    if ans_list[i] == max_v:
        print(i+1, end=' ')