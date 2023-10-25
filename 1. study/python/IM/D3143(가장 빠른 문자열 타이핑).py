import sys
sys.stdin = open('D3143.txt')

T = int(input())
for tc in range(1, T+1):
    A, B = input().split()

    i = j = 0
    N = len(A)
    M = len(B)
    cnt = 0
    while i < N:
        if A[i] != B[j]:
            i -= j
            j = -1

        i += 1
        j += 1

        if j == M:
            cnt += 1
            j = 0

    print(f'#{tc} {N - (M-1) * cnt}')