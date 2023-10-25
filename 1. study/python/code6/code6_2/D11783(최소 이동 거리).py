import sys
sys.stdin = open('D11783.txt')


def dijkstra(s):
    # 시작점 설정
    D[s] = 0
    # 정점의 갯수만큼 선택하기
    for _ in range(V):
        # 최소값 찾기
        min_v = 987654321
        for i in range(V):
            if visited[i] == 0 and min_v > D[i]:
                min_v = D[i]
                v = i  # 너가 젤 작구나
        # 방문체크(선택)
        visited[v] = 1
        # 가중치 갱신 (다음 타겟은 누구?)
        for w in range(V):
            # 좀 더 효율이 좋은 가중치로 덮어쓰기
            if adj[v][w] and not visited[w]:
                if D[w] > D[v] + adj[v][w]:
                    D[w] = D[v] + adj[v][w]

    return


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adj = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N + 1)
    D = [987654321] * (N + 1)  # 가중치
    V = N + 1
    # 인접 행렬 만들기
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w

    dijkstra(0)
    print(f'#{tc} {D[-1]}')
