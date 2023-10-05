import sys
sys.stdin = open('D1949.txt')

def dfs(k, i, j, c): # k 들어간 깊이, c: 깎을 수 있는 기회
    global max_v
    max_v = max(max_v, k)
    visited[i][j] = 1
    for p in range(4):
        ni = i + di[p]
        nj = j + dj[p]

        if 0 <= ni < N and 0<= nj < N and not visited[ni][nj]:
            if arr[ni][nj] < arr[i][j]:
                dfs(k + 1, ni, nj, c)
            else:
                if arr[ni][nj] - arr[i][j] < K and \
                    c == 1:
                    temp = arr[ni][nj] # 되돌릴 때 쓰기 위해 값 저장
                    # 얼마나 깎을 것인가??(갈 곳이 현재 있는 곳의 한칸 아래로 되도록 하는 것이 Best)
                    arr[ni][nj] = arr[i][j] - 1
                    dfs(k + 1, ni, nj, c - 1)
                    # 값 돌려주기
                    arr[ni][nj] = temp

    visited[i][j] = 0

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    # K : 최대 공사 가능 깊이
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    max_v = 0
    # 가장 높은 산 찾기
    high = max(map(max, arr))
    for i in range(N):
        for j in range(N):
            if arr[i][j] == high:
                dfs(1, i, j, 1)

    print(f'#{tc} {max_v}')