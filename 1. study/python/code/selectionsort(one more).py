# def selection_sort(arr, N):
#
#     for i in range(N):
#         # 초기값도 i로!!
#         min_idx = i
#         for j in range(i+1, N):
#             if arr[min_idx] > arr[j]:
#                 min_idx = j
#         # 여기 위치랑, 바꾸는 값들 기억할 것!!
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#
#     return arr
#
#
# arr = [7, 4, 2, 8, 11, 3, 19]
# N = len(arr)
# print(selection_sort(arr, N))

#----------------------------------------------------------------------
def selection_sort(arr, N):
    pass


arr = [7, 4, 2, 8, 11, 3, 19]
N = len(arr)
print(selection_sort(arr, N))