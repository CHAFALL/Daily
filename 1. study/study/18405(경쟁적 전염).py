# 낮은 숫자가 큰 숫자를 만나면 갱신하도록
# 다만 같은 초일 때만.
# 바이러스를 que에 넣어서 한 방에 터트리기
# 튜플 필요없고 그냥 작은 숫자를 앞에가도록 처음에 넣고 퍼트리면 끝
from collections import deque


def bfs():
    temp = [] # 바이러스 종류, 바이러스 위치
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                temp.append((arr[i][j], i, j))
    # 번호 빠른 놈들이 먼저 자리 차지
    temp.sort()
    Q = deque(temp)
    while Q:
        v = Q.popleft()
        # 할 일
        print(v)
        arr[v[1]][v[2]] = v[0]
        for k in range(4):
            nr = v[1] + dr[k]
            nc = v[2] + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] != 0:
                    Q.append((v[0], nr, nc))

    return



dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
N, K = map(int, input().split()) # K: 바이러스 번호
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

bfs()

print(arr)
print(arr[X-1][Y-1])

