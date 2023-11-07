'''
100 40021
'''
'''
4 42
'''
# BFS

from collections import deque

def bfs(v):
    Q = deque([v])
    visited[v] = 1

    while Q:
        v = Q.popleft()
        # 하고 싶은 일
        if v == B:
            return visited[v]

        for w in [v * 2, v * 10 + 1]:
            if w <= B and visited[w] == 0:
                Q.append(w)
                visited[w] = visited[v] + 1

    return -1

A, B = map(int, input().split())
visited = [0] * (B + 1)
print(bfs(A))

#------------------------------------------------------------
