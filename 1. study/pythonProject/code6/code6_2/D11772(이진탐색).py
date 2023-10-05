import sys
sys.stdin = open('D11772.txt')


def binarysearch(key):
    dir = 0  # 방향(왼쪽:-1, 초기값:0, 오른쪽:1)
    low = 0
    high = N - 1
    while low <= high:
        mid = (low + high) // 2
        # 탐색 성공
        if A[mid] == key:
            return 1
        # 더 작은 값에서 찾아봐
        elif key < A[mid]:
            if dir == -1:
                return 0
            high = mid - 1
            dir = -1

        # 더 큰 값에서 찾아봐
        elif key > A[mid]:
            if dir == 1:
                return 0
            low = mid + 1
            dir = 1

    return 0


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 이진 탐색은 정렬이 필수!!
    A.sort()

    cnt = 0
    for i in range(M):
        cnt += binarysearch(B[i])

    print(f'#{tc} {cnt}')
