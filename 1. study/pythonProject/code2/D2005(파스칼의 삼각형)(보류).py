import sys
sys.stdin = open('D2005.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())



# T = int(input())
#
# SIZE = 100
# memo = [[0] * SIZE for _ in range(SIZE)]
# for i in range(SIZE):
#     for j in range(i + 1):
#         if j == 0 or i == j:
#             memo[i][j] = 1
#         else:
#             memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]
#
# for tc in range(1, T + 1):
#     N = int(input())
#     # 출력
#     print(f'#{tc}')
#     for i in range(N):
#         for j in range(i + 1):
#             print(f'{memo[i][j]}', end=' ')
#         print()