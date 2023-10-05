import sys
sys.stdin = open('D1486.txt')

# #부분 집합 문제, 가지치기 필수
# def f(i, N, s): # s : i-1 원소까지 부분집합의 합(포함된 원소의 합)
#     global min_gap
#     if min_gap == 0:
#         return
#     if s >= B:
#         if min_gap > s - B:
#             min_gap = s - B
#
#     elif i == N:   # 남은 원소가 없는 경우
#         return
#     else:
#         bit[i] = 1           # 부분집합에 A[i] 포함
#         f(i + 1, N, s + arr[i])
#         bit[i] = 0          # 부분집합에 A[i] 미포함
#         f(i + 1, N, s)
#         return
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, B = map(int, input().split())
#     arr = list(map(int, input().split()))
#     min_gap = 987654321
#
#
#     f(0, N, 0)
#
#     print(f'#{tc} {min_gap}')
#
#----------------------------------------------------------------
# 강사님 풀이

# 중복 미포함?는 트리 방식(뽑고, 안 뽑고로 구별)이 좋다??(for 보단..)

def recur(level, acc_height): # s : i-1 원소까지 부분집합의 합(포함된 원소의 합)
    global ans

    # 가지치기
    # 현재까지 합이 선반 높이를 넘어간다면
    # 앞으로는 더 볼 필요 x
    if acc_height >= B:
        ans = min(ans, acc_height)
        return
    # 기저 조건
    if level == N:
        return

    # 해당 점원을 탑에 쓸 경우
    recur(level + 1, acc_height + arr[level])
    # 안 쓸 경우
    recur(level + 1, acc_height)



T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = int(1e9)

    recur(0, 0)

    print(f'#{tc} {ans - B}')
