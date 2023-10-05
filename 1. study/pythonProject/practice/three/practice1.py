# # 이진 탐색 - 반복문
# arr = [2, 4, 7, 9, 11, 19, 23]
#
# # 문제에서 데이터가 정렬되어 있다 라는 조건이 없다면
# # 반드시 정렬을 먼저 수행해야 한다.
# arr.sort()
#
# def binarySearch(target):
#     low = 0
#     high = len(arr) - 1
#     # low > high 라면 데이터를 못 찾은 경우
#     while low <= high:
#         mid = (low + high) // 2
#
#         # 1. 가운데 값이 정답인 경우
#         if arr[mid] == target:
#             return mid
#         # 2. 가운데 값이 정답보다 작은 경우
#         elif arr[mid] < target:
#             low = mid + 1
#         # 3. 가운데 값이 정답보다 큰 경우
#         else:
#             high = mid - 1
#
#     return "해당 데이터는 없습니다"
#
# print(f'9 = {binarySearch(9)}')
# print(f'4 = {binarySearch(4)}')
# print(f'10 = {binarySearch(10)}')

#------------------------------------------------------
# 이진 검색 - 재귀 호출 활용

# 이진 탐색 - 반복문
arr = [2, 4, 7, 9, 11, 19, 23]

# 문제에서 데이터가 정렬되어 있다 라는 조건이 없다면
# 반드시 정렬을 먼저 수행해야 한다.
arr.sort()

# 함수 한 번 호출 될때 마다 low, high 변수가 바뀌어서 사용되어서 인자로 넣음
def binarySearch(low, high, target):
    # 기저 조건: 언데까지 재귀호출을 반복할 것인가 ?
    # low > high 라면 데이터를 못참음
    if low > high:
        return -1
    mid = (low + high) // 2

    # 1. 가운데 값이 정답인 경우
    if target == arr[mid]:
        return mid
    # 2. 가운데 값이 정답보다 작은 경우
    elif arr[mid] < target:
        return binarySearch(mid + 1, high, target)
    # 3. 가운데 값이 정답보다 큰 경우
    else:
        return binarySearch(low, mid-1, target)

print(f'9 = {binarySearch(0, len(arr)-1, 9)}')
print(f'4 = {binarySearch(0, len(arr)-1, 4)}')
print(f'10 = {binarySearch(0, len(arr)-1, 10)}')

#재귀 쉽게 조건 작성하는 팁
# 먼저 기저 조건 작성, 그리고 재귀를 안 돌아도 될 경우를 생각해라