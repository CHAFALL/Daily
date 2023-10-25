import sys
sys.stdin = open('D1251.txt')

def prim(s):
    D[s] = 0
    # 정점의 갯수만큼 선택하기
    for _ in range(N):
        # 최소값 찾기
        min_v = 2_000_000**2
        for i in range(N):
            if visited[i] == 0 and min_v > D[i]:
                min_v = D[i]
                v = i # 정점 선택

        # 방문처리(선택)
        visited[v] = 1
        # 인접 정점의 가중치 갱신
        for w in range(N):
            if adj[v][w] and not visited[w]:
                if D[w] > adj[v][w]:
                    D[w] = adj[v][w]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    visited = [0] * N
    D = [2_000_000**2] * N # 가중치
    adj = [[0] * N for _ in range(N)]

    # 인접 행렬 만들기
    for i in range(N):
        for j in range(N):
            # 자기 자신은 빼기
            if i == j:
                continue
            adj[i][j] = E *((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)

    prim(0)
    print(f'#{tc} {sum(D):.0f}')
