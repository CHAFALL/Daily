import sys
sys.stdin = open('D1970.txt')

WON = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 카운트 배열
    C = [0] * 8

    i = 0
    while i < 8:
        if N - WON[i] >= 0:
            N -= WON[i]
            C[i] += 1
        else:
            i += 1

    print(f'#{tc}')
    print(*C)
