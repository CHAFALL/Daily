# 키 삽입과 제거
def modify_key(x, y, M, key, board, insert_key):
    for i in range(M):
        for j in range(M):
            if insert_key:
                board[x+i][y+j] += key[i][j]
            else:
                board[x+i][y+j] -= key[i][j]

# 가능여부 파악
def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M + i][M + j] != 1:
                return False
    return True

# 90도 회전
def rotate(arr):
    return list(zip(*arr[::-1]))

def solution(key, lock):

    M, N = len(key), len(lock)

    # 인덱스 에러 방지를 위해 0 패딩
    board_size = M * 2 + N
    board = [[0] * board_size for _ in range(board_size)]
    # 좌물쇠 중앙에 배치
    for i in range(N):
        for j in range(N):
            board[M + i][M + j] = lock[i][j]

    # 회전 4번
    for _ in range(4):
        for i in range(1, M + N):
            for j in range(1, M + N):
                # 열쇠 삽입
                modify_key(i, j, M, key, board, True)
                # 가능 여부 파악
                if check(board, M, N):
                    return True
                # 열쇠 제거
                modify_key(i, j, M, key, board, False)
        # 열쇠 90도 회전
        key = rotate(key)

    # 가능한 것이 없다면?
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))