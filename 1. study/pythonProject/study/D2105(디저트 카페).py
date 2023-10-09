import sys
sys.stdin = open('D2105.txt')
# 깊이, 좌표, 지금까지 챙긴 디저트 종류, 방향
# def dfs(k, i, j, p, d):
#     global max_v
#     if d > 3:
#         return
#     if d == 3 and si == i and sj == j:
#         max_v = max(max_v, k)
#         return
#
#     ni = i + di[d]
#     nj = j + dj[d]
#     if 0 <= ni < N and 0 <= nj < N:
#         # 중복이 아니라면 챙기고 전진
#         if arr[ni][nj] not in p:
#             dfs(k + 1, ni, nj, p+[arr[ni][nj]], d)
#         # 중복이라면 방향 바꾸기
#         else:
#             dfs(k, i, j, p, d + 1)
#
#
#
# di = [1, 1, -1, -1]
# dj = [1, -1, -1, 1]
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     max_v = 0
#     # 양 끝은 할 수가 없음
#     for i in range(0, N - 2):
#         for j in range(1, N - 1):
#             si = i
#             sj = j  # 시작점 저장
#             dfs(1, i, j, [], 0)
#
#     # 디저트를 먹을 수 없는 경우
#     if max_v < 4:
#         max_v = -1
#
#     print(max_v)
#
#위의 방식 틀린 이유!! 중복이 아니더라도 꺽어야 되는 경우가 있다!!

# 깊이, 좌표, 지금까지 챙긴 디저트 종류, 방향
def dfs(k, i, j, p, d):
    global max_v
    if d > 3:
        return
    if d == 3 and si == i and sj == j:
        max_v = max(max_v, k)
        return

    ni = i + di[d]
    nj = j + dj[d]
    # 나가지 않고 중복이 없을 때만 전진이 가능하다.
    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in p:
        dfs(k + 1, ni, nj, p + [arr[ni][nj]], d)
    # 꼭 중복이 아니더라도 꺾어도 된다.(이거때문에 애 먹음)
    dfs(k, i, j, p, d + 1)


di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    # 양 끝은 할 수가 없음
    for i in range(0, N - 2):
        for j in range(1, N - 1):
            si = i
            sj = j  # 시작점 저장
            dfs(0, i, j, [], 0)

    # 디저트를 먹을 수 없는 경우
    if max_v < 4:
        max_v = -1

    print(f'#{tc} {max_v}')
