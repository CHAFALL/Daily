import sys
sys.stdin = open('D11633')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))


    max_v = 0
    min_v = 300000000000
    for i in range(N-M+1):

        temp = 0
        for j in range(i, i + M):
            temp += arr[j]

        if max_v < temp:
            max_v = temp

        if min_v > temp:
            min_v = temp

    print(f'#{tc} {max_v -min_v}')



