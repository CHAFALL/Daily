import sys
sys.stdin = open('D11763.txt')


# def perm(N, k):  # 원소의 개수, 깊이
#     global ans
#     if k == N:
#         temp = 0
#         for i in range(N):
#             temp += arr[p[i] - 1][p[i + 1] - 1]
#         if ans > temp:
#             ans = temp
#     else:
#         for i in range(N):
#             if visited[i] == 0:
#                 visited[i] = 1
#                 p[k] = A[i]
#                 perm(N, k + 1)
#                 visited[i] = 0
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     A = list(range(1, N + 1))
#     ans = 9999999999
#     p = [0] * (N + 1)
#     p[0] = p[N] = A[0]
#     visited = [0] * N
#     # 자기자신을 빼고 순열
#     visited[0] = 1
#     perm(N, 1)
#     print(f'#{tc} {ans}')

#---------------------------------------------------------------------
# 가지치기 포함 (교수님) 최대값은 가지치기 못하므로 주로 최소값으로 문제 냄
def calc(cursum):
    global ans
    # temp = 0
    # for i in range(N):
    #     temp += dist[p[i]][p[i + 1]]
    # if ans > temp:
    #     ans = temp
    cursum += dist[p[N-1]][p[N]]  # 0-1-2 까지만 포함되어있어서 2-0까지 추가
    ans = min(ans, cursum)


def perm(N, k, cursum):  # 원소의 개수, 깊이
    if ans < cursum:
        return

    if N == k:
        calc(cursum)
    else:
        for i in range(N):
            if v[i] == 0:
                v[i] = 1
                p[k] = A[i]
                perm(N, k + 1, cursum + dist[p[k-1]][p[k]])
                v[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    dist = [list(map(int, input().split())) for _ in range(N)]

    A = list(range(N))

    p = [0] * N + [0]  # 임의로 붙었음을 표시 할려고 # 0 1 2 0 으로 저장(출발, 도착 고정)
    # p[0] = p[N] = A[0] # 이거 없어도 됨 (그냥 가독성 느낌인가?)
    v = [0] * N
    v[0] = 1  # 0번은 제외

    ans = 9999999999
    perm(N, 1, 0)
    print(f'#{tc} {ans}')
