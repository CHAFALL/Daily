import sys
sys.stdin = open('D11779.txt')

# 방문체크 하는 이유: 나왔던 애는 쳐낼려고, 그래서 내가 cnt로 할 때 값이 커졌던거네...

from collections import deque
def bfs(v):
    Q = deque()  # Q = deque([v]) 이거도 됨
    Q.append(v)
    visited[v] = 1

    while Q:
        v = Q.popleft()

        if v == M:
            print(f'#{tc} {visited[v]-1}')
            return

        for w in [v + 1, v - 1, v * 2, v - 10]:  # 인접한 정점 만들기
            if 1 <= w <= 1_000_000 and visited[w] == 0:  # 이거 순서 반대로 되면 안됨
                Q.append(w)
                visited[w] = visited[v] + 1

    return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1_000_001
    bfs(N)
#-----------------------------------------------------------------
# 교수님 풀이
# from collections import deque
#
#
# def bfs(n, m):
#     Q = deque([n])  # Q = deque(); Q.append(n)
#     visited[n] = 1
#     while Q:
#         n = Q.popleft()
#         if n == m:
#             return visited[n] - 1
#         for w in [n + 1, n - 1, n * 2, n - 10]:
#             if 0 < w <= 1_000_000:
#                 if visited[w] == 0:
#                     Q.append(w)
#                     visited[w] = visited[n] + 1
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     visited = [0] * (1_000_000 + 1)
#     print(f'#{tc} {bfs(N, M)}')