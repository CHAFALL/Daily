import copy

# 전체 - 감시 지역 = 사각지대

# 딕셔너리로 cctv 방향을 선정
cctv = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]]
}

# 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cctv_list = []
for i in range(N):
    for j in range(M):
        if 0< arr[i][j] < 6:
