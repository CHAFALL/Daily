import sys
sys.stdin = open('D2117.txt')

T = int(input())
for tc in range(1, T + 1):
    # 도시의 크기, 하나의 집이 지불할 수 있는 비용
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for si in range(N):
        for sj in range(N):
            for k in range(1, 2 * N):
                cnt = 0
                for i in range(si - k + 1, si + k):
                    for j in range(sj - k + 1 + abs(i - si), sj + k - abs(i - si)):
                        if 0 <= i < N and 0 <= j < N:
                            if arr[i][j] == 1:
                                cnt += 1
                cost = k * k + (k - 1) * (k - 1)
                if cost <= cnt * M:
                    max_v = max(max_v, cnt)

    print(f'#{tc} {max_v}')
#---------------------------------------------------------------------------
# 마름모 연습(농작물)
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    total = 0
    s = e = N // 2
    for i in range(N):
        for j in range(s, e + 1):
            total += arr[i][j]
        if i < N // 2 :
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    print(f'#{tc} {total}')
