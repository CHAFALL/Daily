import sys
sys.stdin = open('D11646')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        max_h = N - 1 - i
        for j in range(i+1, N):
            if arr[i] <= arr[j]:
                max_h -= 1

        # 여기서 실수함
        if ans < max_h:
            ans = max_h

    print(f'#{tc} {ans}')


