import sys
sys.stdin = open('D11718.txt')

# di = [0, 1, 1, 1, 0, -1, -1, -1]
# dj = [1, 1, 0, -1, -1, -1, 0, 1]
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     # 0: 빈 공간, 1: 사냥꾼, 2: 토끼, 3: 바위
#     counts = 0
#     for i in range(N):
#         for j in range(N):
#             # 사냥꾼이면 검토 시작
#             if arr[i][j] == 1:
#                 for k in range(8):
#                     p = 1
#                     while True:
#                         ni = i + di[k] * p
#                         nj = j + dj[k] * p
#                         if 0 <= ni < N and 0 <= nj < N:
#                             # 토끼이면 죽이고(빈 공간으로 변경), 카운트 1
#                             if arr[ni][nj] == 2:
#                                 counts += 1
#                                 arr[ni][nj] = 0
#                             # 바위 만나면 나가기
#                             elif arr[ni][nj] == 3:
#                                 break
#                         # 밖으로 나가면 나가기
#                         else:
#                             break
#                         p += 1
#
#     print(f'#{tc} {counts}')
#---------------------------------------------------------------------------------------
# 연습
di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 0: 빈공간, 1: 사냥꾼, 2: 토끼, 3: 바위
    cnt = 0
    for i in range(N):
        for j in range(N):
            # 사냥꾼이면 탐색 시작
            if arr[i][j] == 1:
                for k in range(8):
                    p = 1
                    while True:
                        ni = i + di[k] * p
                        nj = j + dj[k] * p
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 2:
                                arr[ni][nj] = 0
                                cnt += 1
                            elif arr[ni][nj] == 3:
                                break
                        else:
                            break
                        p += 1
    print(cnt)



