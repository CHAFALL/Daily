# 다시 거쳐도 되므로 visited는 필요 없음
def dfs(i, j, n, p):
    global p_set
    if n == 6:
        p_set.add(''.join(p))
        return
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            dfs(ni, nj, n+1, p+[arr[ni][nj]])

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = 5
arr = [list(input().split()) for _ in range(N)]
p_set = set()
p = []
for i in range(N):
    for j in range(N):
        dfs(i, j, 1, p+[arr[i][j]])

print(len(p_set))

