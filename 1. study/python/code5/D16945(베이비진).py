import sys

sys.stdin = open('D16945.txt')


# def perm(k, N): # k 현재 깊이, N 목표
#     global ans
#     if k == N:
#         # 3등분 하고 triple, run인지 체크
#         if arr[0] == arr[1] == arr[2]:
#             if (arr[3] == arr[4] == arr[5]) or (arr[3] + 2 == arr[4] + 1 == arr[5]):
#                 ans = 1
#                 return
#         elif arr[0] + 2 == arr[1] + 1 == arr[2]:
#             if (arr[3] == arr[4] == arr[5]) or (arr[3] + 2 == arr[4] + 1 == arr[5]):
#                 ans = 1
#                 return
#
#     else:
#         for i in range(k, N):
#             arr[k], arr[i] = arr[i], arr[k]
#             perm(k+1, N)
#             arr[k], arr[i] = arr[i], arr[k]
#
#
# T = int(input())
# for tc in range(1, T+1):
#     arr = list(map(int, input()))
#     N = len(arr)
#     ans = 0
#     perm(0, N)
#     print(f'#{tc} {ans}')
# ====================================================================================
def baby_gin():
    global ans
    check = 0
    # triplet
    if p[0] == p[1] and p[1] == p[2]: check += 1
    if p[3] == p[4] and p[4] == p[5]: check += 1
    # run
    if p[0] + 1 == p[1] and p[1] + 1 == p[2]: check += 1
    if p[3] + 1 == p[4] and p[4] + 1 == p[5]: check += 1

    if check == 2:
        ans = 1
        return


def perm(n, k):
    if n == k:
        baby_gin()
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                p[k] = arr[i]
                perm(n, k + 1)
                visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input()))
    N = len(arr)
    visited = [0] * N
    p = [0] * N

    ans = 0
    perm(N, 0)
    print(f'#{tc} {ans}')
