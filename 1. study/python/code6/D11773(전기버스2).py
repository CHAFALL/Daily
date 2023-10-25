import sys
sys.stdin = open('D11773.txt')

# def bt(cnt, k): # k: 위치
#     global ans
#
#     # 가지 치기
#     if ans <= cnt:
#         return
#
#     if k >= N - 1: # 넘어가도 클리어
#         if ans > cnt:
#             ans = cnt
#         return
#
#     rng = arr[k]
#     while rng:
#         bt(cnt + 1, k + rng)
#         rng -= 1
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, *arr = list(map(int, input().split()))
#     ans = 999999999
#
#     bt(0, 0)
#     print(f'#{tc} {ans-1}')
#-------------------------------------------------------------
def bt(cnt, k, battery):  # k: 위치
    global ans

    # 가지 치기
    if ans <= cnt:
        return

    if k == N - 1:
        if ans > cnt:
            ans = cnt
        return


    # 배터리가 있을 때만 충전 안하고 갈 수 있음.
    # (배터리가 없으면 반드시 충전해야 됨)
    if battery:
        bt(cnt, k + 1, battery - 1)
    # 충전을 할 경우(이건 선택 사항임)
    bt(cnt + 1, k + 1, arr[k] - 1)


T = int(input())
for tc in range(1, T + 1):
    N, *arr = list(map(int, input().split()))
    ans = 999999999
    # 처음은 반드시 들림
    bt(0, 1, arr[0] - 1)
    print(f'#{tc} {ans}')
#-----------------------------------------------------------------
# 교수님 풀이
# def dfs(n, k, e, c):
#     global ans
#     if ans <= c: return
#     if n == k:
#         if ans > c:
#             ans = c
#             return
#     else:
#         # 충전o
#         dfs(n, k + 1, arr[k] - 1, c + 1)
#         # 충전X, e가 0보다는 커야한다.
#         if e > 0:
#             dfs(n, k + 1, e - 1, c)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     arr = list(map(int, input().split()))
#     ans = 987654321
#     dfs(arr[0], 2, arr[1] - 1, 0)
#     print(f'#{tc} {ans}')