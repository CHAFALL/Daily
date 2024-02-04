import sys
sys.setrecursionlimit(10**6)


def dfs(node, distance):
    for next_node, w in tree[node]:
        # 아직 방문하지 않은 노드라면
        if visited[next_node] == -1:
            visited[next_node] = distance + w
            dfs(next_node, distance + w)


N = int(input()) # 노드의 개수
tree = [[] for _ in range(N + 1)]  # 루트 노드 1부터
visited = [-1] * (N + 1)
for _ in range(N - 1):
    p, c, w = map(int, input().split()) # 부모, 자식, 가중치
    tree[p].append([c, w])

visited[1] = 0
dfs(1, 0)







