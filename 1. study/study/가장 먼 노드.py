from collections import deque

def bfs(tree, visited, start):
    # 방문체크
    visited[1] = 1
    Q = deque()
    Q.append(1)

    while Q:
        v = Q.popleft()
        for w in tree[v]:
            # 방문을 안 했더라면
            if not visited[w]:
                # 거리만큼 더해주기 (실제론 1 적음)
                visited[w] += visited[v] + 1
                Q.append(w)



def solution(n, edge):
    answer = 0

    # 간선의 개수
    m = len(edge)

    visited = [0] * m

    tree = [[] for _ in range(n + 1)]


    for i in range(m):
        a, b = edge[i]
        # 양방향
        tree[a].append(b)
        tree[b].append(a)

    bfs(tree, visited, 1)

    # 가장 먼 거리 구하기
    max_v = max(visited)

    # 가장 먼 거리인 노드 구하기
    for i in range(n + 1):
        if visited[i] == max_v:
            answer += 1


    return answer




print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))