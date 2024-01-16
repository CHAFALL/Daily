from collections import deque

def bfs():
    Q = deque()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                Q.append((i, j))




N = int(input())
# 1, 2, 3, 4, 5, 6 : 물고기 크기, 0: 빈칸, 9: 아기상어 위치

arr = [list(map(int, input().split())) for _ in range(N)]

bfs()

