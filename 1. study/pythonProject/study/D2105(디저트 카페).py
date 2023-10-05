import sys
sys.stdin = open('D2105.txt')
# 깊이, 좌표, 지금까지 챙긴 디저트 종류, 방향
def dfs(k, i, j, p, d):
    global max_v
    max_v = max(max_v, k)

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if 0<= ni < N and 0<= nj < N:
            if arr[ni][nj] not in p:
                dfs(k + 1, ni, nj, p+[arr[ni][nj]], d)
            else:
                dfs(k + 1, ni, nj, p+[arr[ni][nj]], d + 1)



di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    # 양 끝은 할 수가 없음
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            dfs(1, i, j, [], 0)

    # 디저트를 먹을 수 없는 경우
    if max_v < 4:
        max_v = -1

    print(max_v)