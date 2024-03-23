import copy

# 한 대의 ccty가 감시하는 것
def monitor(arr_copy, type1, i, j, cnt): # type1: cctv가 감시할 수 있는 방향 중 한 덩어리
    for p1 in type1:
        ni = i
        nj = j  # 초기화를 위해

        while True:
            ni += di[p1]
            nj += dj[p1]
            # 종료 조건 :  나가거나 벽을 만났을 때
            if not (0<= ni < N and 0<= nj < M) or arr_copy[ni][nj] == 6:
                break

            elif arr_copy[ni][nj] == 0:
                arr_copy[ni][nj] = 9
                cnt += 1

    return cnt



def solve(v, count):
    global max_count
    if v == cctv_count:
        max_count = max(max_count, count)
        return

    arr_copy = copy.deepcopy(arr)
    i, j, type = cctv_list[v]
    for p in cctv[type]:
        cnt = monitor(arr_copy, p, i, j, 0)
        solve(v + 1, count + cnt)
        # arr_copy = copy.deepcopy(arr)


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
total = N * M  # 전체 - 감시 지역 = 사각지대
cctv_count = 0
for i in range(N):
    for j in range(M):
        if 0< arr[i][j] < 6:
            cctv_list.append((i, j, arr[i][j]))
            cctv_count += 1
            total -= 1
        elif arr[i][j] == 6:
            total -= 1

max_count = 0
solve(0, 0)
print(total - max_count)

#------------------------------------------------------
# import copy
#
# # 한 대의 ccty가 감시하는 것
# def monitor(i, j, type):
#
#
# def solve(v):
#     global min_count
#     if v == cctv_count:
#         count = 0
#         for i in range(N):
#             for j in range(M):
#                 if arr[i][j] == 0:
#                     count += 1
#
#         min_count = min(count, min_count)
#         return
#
#     arr_copy = copy.deepcopy(arr)
#     i, j, type = cctv_list[v]
#     for p in cctv[type]:
#         print(p)
#         monitor(p, i, j)
#         solve(v + 1)
#
#
# # 딕셔너리로 cctv 방향을 선정
# cctv = {
#     1: [[0], [1], [2], [3]],
#     2: [[0, 2], [1, 3]],
#     3: [[0, 1], [1, 2], [2, 3], [3, 0]],
#     4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
#     5: [[0, 1, 2, 3]]
# }
#
# # 상 우 하 좌
# di = [-1, 0, 1, 0]
# dj = [0, 1, 0, -1]
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# cctv_list = []
# cctv_count = 0
# for i in range(N):
#     for j in range(M):
#         if 0 < arr[i][j] < 6:
#             cctv_list.append((i, j, arr[i][j]))
#             cctv_count += 1
#
# min_count = 99999999