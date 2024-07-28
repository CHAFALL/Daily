# 딜이나 힐 싹 다 누적해서 한 방에 터트리는 방식으로 해보자.
# 누적 합 이용. (IMOS법)

# 누적합 배열 만들기
def make(N, M, array, skill):
    for sk in skill:
        type = sk[0]; r1 = sk[1]; c1 = sk[2]
        r2 = sk[3]; c2 = sk[4]; degree = sk[5]

        # 딜이면 -1 힐이면 1
        sign = -1 if type == 1 else 1

        array[r1][c1] += sign * degree
        array[r1][c2 + 1] -= sign * degree
        array[r2 + 1][c1] -= sign * degree
        array[r2 + 1][c2 + 1] += sign * degree

    # 가로로 한번, 세로로 한번 휩쓸기

    for i in range(N):
        for j in range(M):
            array[i][j + 1] += array[i][j]

    for j in range(M):
        for i in range(N):
            array[i + 1][j] += array[i][j]

    return

# 딜 : 1, 힐 : 2
# [type, r1, c1, r2, c2, degree]
def solution(board, skill):

    N = len(board) # 행
    M = len(board[0]) # 열

    # 누적합 배열 생성
    prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
    make(N, M, prefix_sum, skill)

    answer = 0
    for i in range(N):
        for j in range(M):
            if prefix_sum[i][j] + board[i][j] > 0:
                answer += 1


    return answer


print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
