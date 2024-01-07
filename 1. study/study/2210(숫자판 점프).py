# 다시 거쳐도 되므로 visited는 필요 없음
def dfs(i, j, n, p):
    global p_set
    if n == 6:
        # 문자열로 이루어진 리스트를 하나의 문자열로 바꾸고
        # set에 넣어줘서 중복 제거
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
p = []  #숫자판
for i in range(N):
    for j in range(N):
        dfs(i, j, 1, p+[arr[i][j]])

print(len(p_set))

