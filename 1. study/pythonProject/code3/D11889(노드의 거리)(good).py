import sys
sys.stdin = open('D11889.txt')

def bfs(v):
    Q = []
    Q.append(v)
    visited[v] = 1
    while Q:
        v = Q.pop(0)
        if v == G:
            return visited[v] - 1
        for w in range(1, V+1):
            if adj_m[v][w] == 1 and visited[w] == 0:
                Q.append(w)
                visited[w] = visited[v] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 초기 설정
    adj_m = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    # 인접 행렬 만들기
    for _ in range(E):
        s, e = map(int, input().split())
        adj_m[s][e] = adj_m[e][s] = 1

    S, G = map(int, input().split())

    print(bfs(S))
