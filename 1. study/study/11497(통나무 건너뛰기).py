T = int(input())
for _ in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 인덱스 차이 2로 나도록 구하기

    arr.sort()
    max_gap = 0
    for i in range(N - 2):
        max_gap = max(max_gap, abs(arr[i + 2] - arr[i]))

    print(max_gap)
