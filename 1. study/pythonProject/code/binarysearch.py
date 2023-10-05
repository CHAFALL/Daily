def binarysearch(arr, N, key):
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        # 검색 성공
        if arr[mid] == key:
            return True
        # 더 큰 곳에서 찾아봐
        if arr[mid] < key:
            start = mid + 1
        # 더 작은 곳에서 찾아봐
        if arr[mid] > key:
            end = mid -1

    return False


arr = [2, 4, 6, 8, 10, 12, 14, 17]
N = len(arr)
key = 10

print(binarysearch(arr, N, key))


#====================================================================
# def binarysearch(arr, N, key):
#     start = 0
#     end = N-1
#     while start <= end:
#         mid = (start + end) // 2
#         # 검색 성공
#         if arr[mid] == key:
#             return True
#         # 더 큰 값에서 찾아봐
#         elif arr[mid] < key:
#             start = mid + 1
#         # 더 작은 값에서 찾아봐
#         else:
#             end = mid - 1
#
#     return False
#
#
#
# arr = [2, 4, 6, 8, 11, 12, 14, 17]
# N = len(arr)
# key = 10
#
# print(binarysearch(arr, N, key))
