import sys
sys.stdin = open('D11822')


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    real_counts = 0
    for i in range(1 << 12): # 2^12
        counts = 0
        total = 0
        for j in range(12):# 이렇게 먼저 for을 돌리는구나
            if i & (1<<j):
                counts +=1
                total += A[j]
        if counts == N and total == K:
            real_counts +=1


    print(f'#{tc} {real_counts}')





