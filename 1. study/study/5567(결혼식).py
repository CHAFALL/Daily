# 친구의 친구의 친구부터는 불가능
from collections import deque

def BFS(v, cnt):
    global total
    Q = deque()
    Q.append((v, cnt))
    visited[v] = 1
    while Q:
        v, cnt = Q.popleft()
        for w in tree[v]:
            if not visited[w] and cnt < 2:
                Q.append((w, cnt + 1))
                visited[w] = 1
                total += 1


N = int(input())
M = int(input())

visited = [0] * (N + 1)
# 인접리스트
tree = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s) # 양방향

total = 0
BFS(1, 0)
print(total)

