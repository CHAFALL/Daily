import sys
sys.stdin = open('D2805.txt')

# 방법 1(좌표로 생각하니깐 개 쉽네...)
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#
#     total = 0
#     s = e = N // 2
#     for i in range(N):
#         for j in range(s, e + 1):
#             total += arr[i][j]
#         if i < N // 2 :
#             s -= 1
#             e += 1
#         else:
#             s += 1
#             e -= 1
#     print(f'#{tc} {total}')

#---------------------------------------------------------
#방법 2
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#
#     total = 0
#     M = N // 2
#     k = 0
#     for i in range(N):
#         for j in range(M - k, M + k + 1):
#             total += arr[i][j]
#         if i < N // 2:
#             k += 1
#         else:
#             k -= 1
#     print(f'#{tc} {total}')
##################################################################
# # 방법 3
# # 중간 좌표인 (M, M)을 기준으로 해서, (i, j)와의 좌표거리가 M이하인 좌표라면 수확을 해도 되는 범위
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#
#     total = 0
#     M = N // 2
#
#     for i in range(N):
#         for j in range(N):
#             if abs(M - i) + abs(M - j) <= M:
#                 total += arr[i][j]
#
#     print(f'#{tc} {total}')
#----------------------------------------------------------------------------------------
# 연습
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    sj = N // 2
    k = 0
    total = 0
    for i in range(N): # 행
        for j in range(sj - k, sj + k + 1):
            total += arr[i][j]
        if i < N // 2:
            k += 1
        else:
            k -= 1
    print(f'#{tc} {total}')
