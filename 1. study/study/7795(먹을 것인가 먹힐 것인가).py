T = int(input())
for _ in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    count = 0
    for i in range(N):
        for j in range(M):
            if A[i] > B[j]:
                count += 1

    print(count)

#-------------------------------------

T = int(input())
for _ in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort()

    count = 0
    for i in range(N):
        for j in range(M):
            if A[i] > B[j]:
                count += 1
            else:
                break

    print(count)
