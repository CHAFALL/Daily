import sys
sys.stdin = open('D4615.txt')

# def solve(i, j, bw):
#     board[i][j] = bw  # 일단 놓고 # 이거 까먹기 쉬움
#     for k in range(8):
#         ni = i + di[k]
#         nj = j + dj[k]
#         temp = []  # 자기랑 같은 색을 만나면 변환
#         while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == op[bw]: # 보드 내부고 반대색이면 계속 이동
#             temp.append((ni, nj))
#             ni = ni + di[k] # 여기 미세하게 다름
#             nj = nj + dj[k]
#         if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == bw: # 보드 내부고 같은 색이면
#             for p, q in temp: # 이렇게 하면 pop 안 써도 되겠네
#                 board[p][q] = bw
#
# # 오호라
# B = 1
# W = 2
#
# di = [0, 1, 1, 1, 0, -1, -1, -1]
# dj = [1, 1, 0, -1, -1, -1, 0, 1]
#
# op = [0, 2, 1] # 이렇게 하는 것도 신기
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     board = [[0] * N for _ in range(N)] # 0 ~ N-1 방식으로 할 것임
#     board[N // 2 - 1][N // 2 - 1] = W
#     board[N // 2 - 1][N // 2] = B
#     board[N // 2][N // 2 - 1] = B
#     board[N // 2][N // 2] = W
#
#     # 그냥 이렇게 다 받은 후에
#     play = [list(map(int, input().split())) for _ in range(M)]
#     # 이렇게 언패킹으로 꺼내면서 넣어주는 방식
#
#     # 사실 이렇게 for문 안에 함수 넣는 것 효율 떨어지긴 함..
#     for col, row, bw in play:
#         solve(row -1, col -1, bw) # 인덱스 고려 잘 할 것!!
#         # 그리고 반대로 들어오는 것도 이렇게 함수로 해서 바꿔주니 좋네
#
#     # 각 테스트 케이스마다 게임이 끝난 후 보드 위의 흑돌, 백돌의 개수를 출력
#     bcnt = wcnt = 0
#     for i in range(N):
#         for j in range(N):
#             if board[i][j] == B:
#                 bcnt += 1
#             elif board[i][j] ==W:
#                 wcnt += 1
#     print(f'#{tc} {bcnt} {wcnt}')

#------------------------------------------------------------------
# 연습
#
# def play(i, j, bw):
#     arr[i][j] = bw # 이거 까먹지 말기
#     for k in range(8):
#         temp = []
#         ni = i + di[k]
#         nj = j + dj[k]
#         while 0 <= ni < N and 0 <= nj < N:
#             if arr[ni][nj] == op[bw]:
#                 temp.append((ni, nj))
#                 ni += di[k]
#                 nj += dj[k]
#             else:
#                 break
#
#         if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == bw:
#             for p, q in temp:
#                 arr[p][q] = bw
#
# di = [0, 1, 1, 1, 0, -1, -1, -1]
# dj = [1, 1, 0, -1, -1, -1, 0, 1]
# op = [0, 2, 1]
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [[0] * N for _ in range(N)]
#     # 초기설정
#     arr[N // 2 - 1][N // 2 - 1] = 2
#     arr[N // 2 - 1][N // 2] = 1
#     arr[N // 2][N // 2 - 1] = 1
#     arr[N // 2][N // 2] = 2
#     # 1: 흑, 2: 백
#     for i in range(M):
#         c, r, bw = map(int, input().split())
#         play(r - 1, c - 1, bw)
#
#     # 최종 확인
#     bcnt = wcnt = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 1:
#                 bcnt+= 1
#             elif arr[i][j] ==2:
#                 wcnt += 1
#
#     print(bcnt, wcnt)
############################################################
# 연습

def play(i, j, color):
    board[i][j] = color # 먼저 놓기 # 까먹지 말기!
    for k in range(8):
        temp = []
        ni = i + di[k]
        nj = j + dj[k]
        while True:
            # 다른 색이면
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == op[color]:
                temp.append((ni, nj))
                # 한번 더 전진
                ni += di[k]
                nj += dj[k]
                # 아래와 같이 하면 되돌리기 귀찮아 짐
                # i = ni
                # j = nj
            else:
                break

        # 같은 색 만나는 순간 # if 위치 잘 보기
        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == color:
            for p, q in temp:
                board[p][q] = color

# 방향
di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]
# 가독성을 위해
B = 1
W = 2
# 신박해서 써봄
op = [0, 2, 1] # 이거 안 쓸려면 if 조건에 그냥 color은 0이 아닐때 추가 하면 됨
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    board = [[0] * N for _ in range(N)]
    #초기설정
    board[N // 2 - 1][N // 2 - 1] = W
    board[N // 2 - 1][N // 2] = B
    board[N // 2][N // 2 - 1] = B
    board[N // 2][N // 2] = W

    # 문제는 r, c 꼴이 아닌 좌표 형식으로 되어있다. (인덱스 시작도 1부터)
    for i in range(M):
        c, r, color = map(int, input().split())
        play(r-1, c-1, color) # 따라서 이렇게 해주면 편함,
        # 단점으론 for문 안에 함수가 있어서 속도 조금 느려짐

    # 다 가지고 논거 갯수 세기
    B_cnt = W_cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == B:
                B_cnt += 1
            elif board[i][j] == W:
                W_cnt += 1

    print(f'#{tc} {B_cnt} {W_cnt}')