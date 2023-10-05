import sys
sys.stdin = open('D11779.txt')

def bfs(n):
    Q = [n]
    visited[n] = 1  # 방문체크

    while Q:
        n = Q.pop(0)
        # 하고 싶은 일
        if n == M:
            return visited[n] - 1
        for w in [n + 1, n - 1, n * 2, n - 10]:
            if 1<= w <=1_000_000 and visited[w] == 0:
                Q.append(w)
                visited[w] = visited[n] + 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited = [0] * 1_000_001
    print(f'#{tc} {bfs(N)}')