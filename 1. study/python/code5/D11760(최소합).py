import sys
sys.stdin = open('D11760.txt')
# # 오른쪽, 아래
# di = [0, 1]
# dj = [1, 0]
#
# def dfs(i, j, sum):
#     global ans
#     # 일단 방문 체크
#
#     if (i, j) == (N-1, N-1):
#         if ans > sum:
#             ans = sum
#         return
#
#     if ans <= sum: # 가지치기
#         return
#
#     for k in range(2):
#         ni = i + di[k]
#         nj = j + dj[k]
#         if 0 <= ni < N and 0 <= nj < N:
#             dfs(ni, nj, sum + arr[ni][nj])
#     return
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # visited = [[0] * N for _ in range(N)]
#     ans = 99999999
#     dfs(0, 0, arr[0][0])
#     print(f'#{tc} {ans}')

#===========================================================
# 교수님 풀이
def dfs(x, y, cursum):
    global ans

    if ans <= cursum:
        return

    if x == N - 1 and y == N - 1:
        ans = min(ans, cursum)
    else:
        if x + 1 < N:
            dfs(x + 1, y, cursum + arr[x + 1][y])
        if y + 1 < N:
            dfs(x, y + 1, cursum + arr[x][y + 1])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321
    dfs(0, 0, arr[0][0])
    print(f'#{tc} {ans}')
