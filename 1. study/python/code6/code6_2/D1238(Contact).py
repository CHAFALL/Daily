import sys
sys.stdin = open('D1238.txt')

def bfs(v):
    Q = [v]
    visited[v] = 1
    while Q:
        v = Q.pop(0)
        for w in adj[v]:
            if visited[w] == 0:
                Q.append(w)
                visited[w] = visited[v] + 1
    return


T = 10
for tc in range(1, T + 1):
    N, start = map(int, input().split())
    temp = list(map(int, input().split()))
    visited = [0] * 101
    adj = [[] for _ in range(101)]
    # 인접 리스트 만들기
    for i in range(N // 2):
        s, e = temp[2 * i], temp[2 * i + 1]
        adj[s].append(e)

    bfs(start)

    max_v = max(visited)

    for i in range(100, -1, -1):
        if visited[i] == max_v:
            print(f'#{tc} {i}')
            break


