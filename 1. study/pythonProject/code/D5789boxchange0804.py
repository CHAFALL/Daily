import sys
sys.stdin = open('D5789')
T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())

        for p in range(L, R+1):
            arr[p-1] = i

    print(f'#{tc}', end = ' ')
    print(*arr)


