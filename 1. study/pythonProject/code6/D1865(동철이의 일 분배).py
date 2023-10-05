import sys
sys.stdin = open('D1865.txt')

# 가지치기 방법: 이미 작은데 곱하면 더 작아지므로 이걸 쳐내면 되네
# def perm(N, k, temp):
#     global max_v
#     # 가지치기
#     if temp <= max_v:
#         return
#     if N == k:
#         if max_v < temp:
#             max_v = temp
#         return
#     # 유도부분
#     else:
#         for i in range(k, N):
#             A[k], A[i] = A[i], A[k]
#             perm(N, k + 1, temp * 0.01 * arr[k][A[k]])
#             A[k], A[i] = A[i], A[k]
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     A = [i for i in range(N)]
#     max_v = 0
#     perm(N, 0, 1)
#     print(f'#{tc} {max_v * 100:.6f}')
#------------------------------------------------------------------
# 방법 2
def f(n, k, s):  # n: 원소의 개수, k: 재귀의 깊이, s: 합
    global max_v
    if max_v >= s:  # 가지치기
        return

    if n == k:  # 순열 완성 => min_v 저장 후 종료
        max_v = s
        return

    else:
        for i in range(n):
            if visited[i] == 0:  # 아직 방문 전이면
                visited[i] = 1  # 방문체크
                f(n, k + 1, s * arr[k][i] * 0.01)
                visited[i] = 0  # 다른 곳에서도 사용할 수 있도록 초기화


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_v = 0
    f(N, 0, 1)

    print(f'#{tc} {max_v * 100:.6f}')