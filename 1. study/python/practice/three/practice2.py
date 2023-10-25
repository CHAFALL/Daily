# # 분할 정복, 병합 정렬
# '''
# 8
# 69 10 30 2 16 8 31 22
# '''
#
#
# # 두 개의 정렬된 부분집합을 하나의 집합으로 만들어 반환
# def merge(left, right):
#     result = []
#     # 병합 과정
#     # 각각의 최소값들(가장 앞쪽 값)을 비교해서 더 작은 요소를 결과에 추가
#     # 두 부분집합에 요소가 없어질 때 까지 계속 반복
#     while left or right:
#         # 두 부분집합의 요소가 모두 남아 있으면
#         if left and right:
#             if left[0] <= right[0]:
#                 result.append(left.pop(0))
#             else:
#                 result.append(right.pop(0))
#         # 왼쪽만 남았을 때
#         elif left:
#             result.append(left.pop(0))  # 하나씩 복사
#             # 한번에 나머지를 뒤에 붙임
#             # result.extend(left)
#             # left.clear()
#         elif right:
#             result.append(right.pop(0))
#
#     return result
#
#
# def merge_sort(a):
#     # basis
#     if len(a) == 1:
#         return a
#     # 유도파트
#     # 문제를 절반으로 나누어서 각각을 정렬
#     else:
#         mid = len(a) // 2
#         left = a[:mid]
#         right = a[mid:]
#
#         left = merge_sort(left)
#         right = merge_sort(right)
#
#         return merge(left, right)
#
#
# N = int(input())
# A = list(map(int, input().split()))
# A = merge_sort(A)  # 병합 정렬은 sorted 느낌의 정렬이므로
#
# print(A)
#--------------------------------------------------------------------------
# 퀵 정렬
'''
9
3 2 4 6 9 1 8 7 5
'''

def hoare_partition(a, l, r):
    p = a[l]
    i, j = l, r
    while i <= j:
        while i <= j and a[i] <= p: # 왼쪽에서 큰 값
            i += 1
        while i <= j and a[j] >= p: # 오른쪽에서 작은 값
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]  # 피봇과 j의 값을 교환

    return j  # 피봇자리

def quick_sort(a, l, r):
    if l < r:
        pivot = hoare_partition(a, l, r)
        # pivot = lomuto_partition(a, l, r)
        quick_sort(a, l, pivot - 1)
        quick_sort(a, pivot + 1, r)

N = int(input())
arr = list(map(int, input().split()))
quick_sort(arr, 0, len(arr)-1)
print(arr) # 얘는 파괴 메소드


#----------------------------------------------------------------
# '''
# 9
# 3 2 4 6 9 1 8 7 5
# '''
# def lomuto_partition(arr, left, right):
#     # 맨 오른쪽 요소를 pivot 으로 설정하고
#     # i = left -1
#     # j = left
#     pivot = arr[right]
#     i = left - 1
#     for j in range(left, right):
#         # arr[j]가 pivot보다 작으면,
#         if arr[j] < pivot:
#             # i를 증가,
#             # arr[j], arr[i] 위치교환
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     # i가 가리키는 위치가 pivot보다 작은값의 마지막 인덱스
#     # i+1 의 위치에 pivot을 두고 i+1 반환
#     arr[i+1], arr[right] = arr[right], arr[i+1]
#     return i+1
#
#
# def hoare_partition(a, l, r):
#     p = a[l]
#     i, j = l, r
#     while i <= j:
#         while i <= j and a[i] <= p: i += 1  # 왼쪽에서 큰값
#         while i <= j and a[j] >= p: j -= 1  # 오른쪽에서 작은값
#         if i < j : a[i], a[j] = a[j], a[i]
#     a[l], a[j] = a[j], a[l]   # 피봇과 j의 값을 교환
#     return j   # 피봇자리
#
#
# def quick_sort(a, l, r):
#     if l < r:
#         # pivot = hoare_partition(a, l, r)
#         pivot = lomuto_partition(a, l, r)
#         quick_sort(a, l, pivot - 1)
#         quick_sort(a, pivot + 1, r)
#
# n = int(input())
# arr = list(map(int, input().split()))
# quick_sort(arr, 0, len(arr)-1)
# print(arr)