# 두고 안 두는 경우 2가지로 분류 해야됨
# 뒀을 때 가능한지 보고,
# def check(i, j):
#     # 8방향 부딪히거나 인덱스 밖으로 나갈 때 까지 쭉 다 가보기
#     for k in range(8):
#         p = 1
#         while True:
#             ni = i + di[k] * p
#             nj = j + dj[k] * p
#
#             if 0 <= ni < N and 0 <= nj < N:
#                 # 부딪힌 애가 있으면 넌 글렀어 나가!
#                 if arr[ni][nj] == 1:
#                     return False
#             # 인덱스 밖으로 나가면? 부딪힌 애가 없네? good 딴 방향도 보자!
#             else:
#                 break
#             # 무조건
#             p += 1
#
#     # 8방향 하나도 안 만났다면? 여기로 옴(퀸을 놓아도 되겠네?)
#     return True
#
#
#     # 원본 되돌리는 것도 필요할 듯
#
#
# # 8방향
# di = [-1, -1, -1, 0, 1, 1, 1, 0]
# dj = [-1, 0, 1, 1, 1, 0, -1, -1]
#


def check(row, col):
    for i in range(row):
        # 기존에 놓았던 퀸 중에서 같은 열에 놓은 곳이 있니?
        # 또는 대각선으로 같은 것이 있니?(두 좌표에서 행 - 행 = 열 - 열이 같으면 같은 대각선임)
        if arr[i] == col or abs(arr[i] - col) == abs(i - row):
            return False

    return True

# 각각의 행마다 퀸은 최대 한 개만 존재함을 이용
def putQueen(row):
    global total
    if row == N:  # 난 애초에 이걸 몰랐어!!
        total += 1
        return

    # 해당 행은 이 열에 놓을 수 있어?
    for col in range(N):
        if check(row, col):
            arr[row] = col # 놓을 수 있으면 놓기
            putQueen(row + 1)  # 다음 행으로 이동


N = int(input())
arr = [0] * N

total = 0
putQueen(0)

print(total)


