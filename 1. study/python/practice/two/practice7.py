'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(v):
    # 시작정점 인큐 + 방문체크
    Q = [v]
    visited[v] = 1

    # 큐가 비어있지 않은 동안
    while Q:
        # v = 디큐
        v = Q.pop(0)
        # 디큐할 때 하고 싶은 일을 하기
        print(v, end=' ')
        # 인접한 정점이고 방문 안한 정점
        for w in range(1, V+1):
            if adj_m[v][w] == 1 and visited[w] == 0:
                # 인큐 + 방문체크
                Q.append(w)
                visited[w] = visited[v] + 1


V, E = map(int, input().split())
temp = list(map(int, input().split()))
adj_m = [[0] * (V+1) for _ in range(V+1)]
visited = [0] * (V+1)
for i in range(E):
    s, e = temp[i*2], temp[i*2+1]
    adj_m[s][e] = adj_m[e][s] = 1  # 무향그래프

bfs(1)
print()
max_i = 0
for i in range(1, V+1):
    if visited[max_i] < visited[i]:
        max_i = i
print(max_i, visited[max_i])