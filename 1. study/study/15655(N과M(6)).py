def comb(n, r, k, s): # s = 시작 숫자
    if r == k:
        print(*p)
    else:
        for i in range(s, n - r + 1 + k):
            p[k] = arr[i]
            comb(n, r, k + 1, i + 1)




N, M = map(int,input().split())
arr = list(map(int, input().split()))
arr.sort()

p = [0] * M
comb(N, M, 0, 0)