import sys
sys.stdin = open('D1860.txt')

T = int(input())
for tc in range(1, T+1):
    # N: 손님 수, M: 걸리는 시간, K: 만드는 붕어빵 수
    N, M, K = map(int, input().split())
    guest = list(map(int, input().split()))
    guest.sort() # 시간 순으로 줄 세우기

    ans = 'Possible'
    for i in range(N):
        if K * (guest[i] // M) - (i+1) < 0:
            ans = 'Impossible'
            break

    print(f'#{tc} {ans}')
