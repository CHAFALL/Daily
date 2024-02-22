# 두고 안 두는 경우 2가지로 분류 해야됨
# 뒀을 때 가능한지 보고,
def check(i, j):
    # 8방향 부딪히거나 인덱스 밖으로 나갈 때 까지 쭉 다 가보기
    for k in range(8):
        p = 1
        while True:
            ni = i + di[k] * p
            nj = j + dj[k] * p

            if 0 <= ni < N and 0 <= nj < N:
                # 부딪힌 애가 있으면 넌 글렀어 나가!
                if arr[ni][nj] == 1:
                    return False
            # 인덱스 밖으로 나가면? 부딪힌 애가 없네? good 딴 방향도 보자!
            else:
                break
            # 무조건
            p += 1

    # 8방향 하나도 안 만났다면? 여기로 옴(퀸을 놓아도 되겠네?)
    return True


    # 원본 되돌리는 것도 필요할 듯
    # 이렇게 하면 되돌리는 것이 안되네...


def putQueen(i, j):
    pass

# 8방향
di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]
N = int(input())
arr = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if check(i, j):
            arr[i][j] = 1




#---------------------
