import sys
sys.stdin = open('D2817.txt')

#
# def f(i, N, s, K):  # s : i-1 원소까지 부분집합의 합(포함된 원소의 합)
#     global cnt
#
#     if s == K:
#         cnt += 1
#         return
#     elif i == N:  # 남은 원소가 없는 경우
#         return
#     elif s > K:  # 더 큰 경우도 멈춰
#         return
#     else:
#         bit[i] = 1  # 부분집합에 A[i] 포함
#         f(i + 1, N, s + arr[i], K)
#         bit[i] = 0  # 부분집합에 A[i] 미포함
#         f(i + 1, N, s, K)
#         return
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     arr = list(map(int, input().split()))
#
#     bit = [0] * N
#     cnt = 0
#     f(0, N, 0, K)
#
#     print(f'#{tc} {cnt}')
#
#----------------------------------------------------------------
# 교수님 풀이1

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0  # 합이 K가 되는 경우의 수
    for i in range(1 << N):  # 부분집합을 표시하는 i
        s = 0
        for j in range(N):  # j번 비트
            if i & (1 << j):  # i의 j번 비트 검사
                s += arr[j]  # 0이 아니면 j번 원소가 부분집합에 포함됨
        if s == K:
            cnt += 1
    print(f'#{tc} {cnt}')

#-------------------------------------------------------------
# 교수님 방식2

def f(i, N, s, K, rs):  # s : i-1 원소까지 부분집합의 합(포함된 원소의 합)
    global cnt

    if i == N:
        if s == K:
            cnt += 1
    elif s > K:  # 더 큰 경우 멈춰
        return
    elif s + rs < K: # 좀 더 강력한 가지치기 (조금 있다가 자세히 배울것임)
        return
    else:
        f(i + 1, N, s + arr[i], K, rs - arr[i])
        f(i + 1, N, s, K, rs - arr[i])


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = 0
    f(0, N, 0, K, sum(arr))

    print(f'#{tc} {cnt}')
