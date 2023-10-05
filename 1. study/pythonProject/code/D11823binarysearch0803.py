import sys
sys.stdin = open('D11823')


def binarysearch(arr, N, key):
    start = 0
    end = N-1
    count = 0
    while start <= end:
        mid = (start + end) // 2
        # 검색 성공
        if arr[mid] == key:
            return count
        # 더 작은 값에서 찾아봐
        elif arr[mid] > key:
            end =  mid - 1
        # 더 큰 값에서 찾아봐
        else:
            start = mid + 1
        count += 1



T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    arr = list(range(1, P+1))
    N = len(arr)

    if binarysearch(arr, N, Pa) > binarysearch(arr, N, Pb):
        print('B')

    elif binarysearch(arr, N, Pa) == binarysearch(arr, N, Pb):
        print(0)
    else:
        print('A')





