import sys
sys.stdin = open('D1208')

T = 10
N = 100
for tc in range(1, T+1):
    dump = int(input())
    arr = list(map(int, input().split()))

    for i in range(dump +1):
        max_idx = min_idx = 0
        for j in range(N):
            if arr[max_idx] <= arr[j]:
                max_idx = j
            if arr[min_idx] >= arr[j]:
                min_idx = j

        if i == dump: # 한번 더 돌려서 정확한 인덱스 값을 찾아야 됨
            break

        arr[max_idx] -= 1
        arr[min_idx] += 1

    print(arr[max_idx] - arr[min_idx])
