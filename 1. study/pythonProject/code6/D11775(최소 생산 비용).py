import sys
sys.stdin = open('D11775.txt')

# def perm(N, k, temp):
#     global min_v
#     # 가지치기
#     if temp >= min_v:
#         return
#     if N == k:
#         if min_v > temp:
#             min_v = temp
#         return
#     # 유도부분
#     else:
#         for i in range(k, N):
#             A[k], A[i] = A[i], A[k]
#             perm(N, k + 1, temp + arr[k][A[k]])
#             A[k], A[i] = A[i], A[k]
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     A = [i for i in range(N)]
#     min_v = 9999999999999
#     perm(N, 0, 0)
#     print(f'#{tc} {min_v}')
#----------------------------------------------------------------
# 교수님 풀이
def perm(N, k, temp):
    global max_v
    # 가지치기
    if temp >= min_v:
        return
    if N == k:
        if min_v > temp:
            min_v = temp
        return
    # 유도부분
    else:
        for i in range(N):
            if visited[i]:
                continue
            visited[i] = 1
            # p[k] = A[i]
            # p[k] = i
            # perm(N, k + 1, temp + arr[k][p[k]])
            perm(N, k + 1, temp + arr[k][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # A = [i for i in range(N)] # 인덱스로 할 때는 이게 없어도 됨
    max_v = 9999999999999
    visited = [0] * N
    # p = [0] * N # 이거도 인덱스로 하면 필요 없어짐
    perm(N, 0, 0)
    print(f'#{tc} {max_v}')
#-------------------------------------------------------------------
# 단비 누나 꺼
# def f(n, k, s):  # n: 원소의 개수, k: 재귀의 깊이, s: 합
#     global min_v
#     if min_v <= s:  # 가지치기
#         return
#
#     if n == k:  # 순열 완성 => min_v 저장 후 종료
#         min_v = s
#         return
#
#     else:  # p[i]에 들어갈 숫자를 결정
#         for i in range(n):
#             if visited[i] == 0:  # 아직 방문 전이면
#                 visited[i] = 1  # 방문체크
#                 f(n, k + 1, s + arr[k][i])
#                 visited[i] = 0  # 다른 곳에서도 사용할 수 있도록 초기화
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = [0] * N  # 이미 선택한 공장인지 표시
#     min_v = 987654321
#     f(N, 0, 0)
#
#     print(f'#{tc} {min_v}')