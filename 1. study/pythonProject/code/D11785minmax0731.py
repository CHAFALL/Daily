import sys
sys.stdin = open('D11785')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = max_idx = 0
    for i in range(N):
        if arr[min_idx] > arr[i]:
            min_idx = i

        if arr[max_idx] < arr[i]:
            max_idx = i
        
    print(arr[max_idx] - arr[min_idx])