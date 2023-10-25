import sys
sys.stdin = open('D3143.txt')

T = int(input())
for tc in range(1, T+1):
    text, pattern = input().split()
    N = len(text)
    M = len(pattern)

    i = 0
    j = 0
    counts = 0
    while i < N:
        if pattern[j] != text[i]:
            i -= j
            j = -1

        i+=1
        j+=1

        if j == M:
            counts += 1
            j = 0

    print(f'#{tc} {N - counts * (M-1)}')