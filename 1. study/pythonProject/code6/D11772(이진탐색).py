import sys
sys.stdin = open('D11772.txt')

# def binarySearch(target):
#     global flag, cnt
#     flag = 2  # 0: 왼쪽, 1: 오른쪽, 2: 초기상태
#     low = 0
#     high = N - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#
#         # 1. 가운데 값이 정답인 경우
#         if arr1[mid] == target:
#             return 1
#         # 2. 가운데 값이 정답보다 작은 경우(오른쪽)
#         elif arr1[mid] < target:
#             # 오오
#             if flag == 1:
#                 return 0
#             low = mid + 1
#             flag = 1
#         # 3. 가운데 값이 정답보다 큰 경우(왼쪽)
#         elif arr1[mid] > target:
#             # 왼왼
#             if flag == 0:
#                 return 0
#             high = mid - 1
#             flag = 0
#
#     # 못 찾은 경우
#     return 0
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr1 = list(map(int, input().split()))
#     arr2 = list(map(int, input().split()))
#     # 이진 탐색은 정렬이 필수
#     arr1.sort()
#     total = 0
#     for i in range(M):
#         total += binarySearch(arr2[i])
#
#     print(f'#{tc} {total}')

#---------------------------------------------------------------
# 교수님 풀이
def binarySearch(a, key):
    low, high = 0, len(a) - 1
    dir = -1 # 방향 미정, 왼쪽 0, 오른쪽 1
    while low <= high:
        mid = (low + high) // 2
        if key == a[mid]:  # 찾았을 때
            return 1
        elif key < a[mid]:  # 왼쪽(0)
            if dir == 0:
                return 0
            high = mid -1
            dir = 0
        else:
            if dir == 1:
                return 0
            low = mid + 1  # 오른쪽(1)
            dir = 1
    return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 이진 탐색은 정렬이 필수
    A.sort()
    cnt = 0
    for i in range(M):
        cnt += binarySearch(A, B[i])

    print(f'#{tc} {cnt}')