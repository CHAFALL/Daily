import sys
sys.setrecursionlimit(10*7)
input = sys.stdin.readline

def dfs(i, j, color):
    # 방문체크
    visited[i][j] = 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if visited[ni][nj] == 0 and arr[ni][nj] == color:
                dfs(ni, nj, color)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

# 'R', 'G', 'B'

cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            cnt += 1
            dfs(i, j, arr[i][j])

# 색약일 때를 위해 초기화
visited = [[0] * N for _ in range(N)]
# 색약인 사람은 빨간색을 초록색으로 본다고 생각
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

cnt2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            cnt2 += 1
            dfs(i, j, arr[i][j])

print(cnt, cnt2)


# ----------------------------------------
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())
matrix = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

three_cnt, two_cnt = 0, 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    #현재 색상 좌표를 방문해준다.
    visited[x][y] = True
    current_color = matrix[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < n) and (0 <= ny < n):
            #현재 좌표의 색상과 상하좌우 좌표에 있는 색상이 같으면 dfs로 넣어준다.
            if visited[nx][ny]==False:
                if matrix[nx][ny] == current_color:
                    dfs(nx,ny)

for i in range(n):
    for j in range(n):
        # 방문하지 않은 좌표이면 dfs로 넣어준다.
        if visited[i][j]==False:
            dfs(i,j)
            three_cnt += 1

#R을 G로 바꾸어준다. --> 적록색약은 같은 색으로 보기 때문에
for i in range(n):
    for j in range(n):
        if matrix[i][j]=='R':
            matrix[i][j]='G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            two_cnt += 1

print(three_cnt,two_cnt)