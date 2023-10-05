def powerset(N, K):
    if N == K:
        sum = 0
        for i in range(N):
            if bit[i] == 1:
                sum += arr[i]
        if sum == 10:
            for i in range(N):
                if bit[i] == 1:
                    print(arr[i], end= ' ')
            print()

    else:
        bit[K] = 1
        powerset(N, K + 1)
        bit[K] = 0
        powerset(N, K + 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
bit = [0] * N # 원소의 포함 여부(0, 1)
powerset(N, 0)