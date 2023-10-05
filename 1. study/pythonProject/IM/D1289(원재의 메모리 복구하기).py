import sys
sys.stdin = open('D1289.txt')

T = int(input())
for tc in range(1, T+1):
    origin = list(map(int, input()))
    N = len(origin)
    bits = [0] * N
    cnt = 0
    for i in range(N):
        if bits[i] != origin[i]:
            for j in range(i, N):
                bits[j] = origin[i]
            cnt+=1
    print(f'#{tc} {cnt}')

