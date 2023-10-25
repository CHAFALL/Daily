'''
물을 기준으로 해서 거리에 따른 값을 표기하고 또 최소이니깐 갱신되도록 하면 될 듯
'''
import sys
sys.stdin = open('D10966.txt')


# bfs는 동시에 퍼트리는 것이 가능!!!!
from collections import deque

def bfs():
    Q = deque()
    for i in range(N):
        for j in range(M):
            # 물이라면 탐색 시작
            if arr[i][j] == 'W':
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 'L':
                        Q.append((i, j))  # 올리고
                        visited[i][j] = 0  # 방문체크
                        break
    while Q:
        i, j = Q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == -1 and arr[ni][nj] == 'L':
                Q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return


di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [str(input()) for _ in range(N)] # str로 바꿔야 합니다.
    visited = [[-1] * M for _ in range(N)]
    bfs()
    total = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] != -1:
                total += visited[i][j]

    print(f'#{tc} {total}')


