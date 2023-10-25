def comb(n, r, k, s): # s는 시작 숫자
    if r == k:
        print(*p)
    else:
        for i in range(s, n):
            p[k] = arr[i]
            comb(n, r, k+1, i)


N, M = map(int, input().split())
arr = list(range(1, N+1))
p = [0] * M
comb(N, M, 0, 0)

