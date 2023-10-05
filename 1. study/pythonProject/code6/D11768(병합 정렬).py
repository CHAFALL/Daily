import sys
sys.stdin = open('D11768.txt')
# from collections import deque
# # 두 개의 정렬된 부분집합을 하나의 집합으로 만들어 반환
# def merge(left, right):
#     global cnt
#     result = []
#     # 병합 과정
#     # 각각의 최소값들(가장 앞쪽 값)을 비교해서 더 작은 요소를 결과에 추가
#     # 두 부분집합에 요소가 없어질 때 까지 계속 반복
#     left = deque(left)
#     right = deque(right)
#     while left or right:
#         # 두 부분집합의 요소가 모두 남아 있으면
#         if left and right:
#             if left[0] <= right[0]:
#                 result.append(left.popleft())
#             else:
#                 result.append(right.popleft())
#         # 왼쪽만 남았을 때
#         elif left:
#             cnt += 1
#             result.extend(left)
#             left.clear()
#         # 오른쪽만 남았을 때
#         elif right:
#             result.extend(right)
#             right.clear()
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
#     # 아래에 else 빼도 됨 (위의 return 때문에 알아서 안 내려감)
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
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     cnt = 0
#     arr = merge_sort(arr) # 병합 정렬은 sorted 느낌의 정렬이므로
#     print(f'#{tc} {arr[N//2]} {cnt}')
#
# 잘못 풀었었는데 왜 맞았지?
#---------------------------------------------------------------
#교수님 풀이

from collections import deque

def merge(left, right):
    left = deque(left)
    right = deque(right)
    result = []
    # 둘 다 남았을 때
    while left and right:
        if left[0] < right[0]:
            result.append(left.popleft())
        else:
            result.append(right.popleft())
    # 왼쪽만 남았을 때
    if left:
        result += left # extend
    # 오른쪽만 남았을 때
    elif right:
        result.extend(right)

    return result

def merge_sort(a):
    global cnt
    # basis
    if len(a) == 1:
        return a
    # 유도 파트
    # 문제를 절반으로 나누어 각각 별도의 정렬 진행
    else:
        mid = len(a) // 2
        left = merge_sort(a[:mid])
        right = merge_sort(a[mid:])

        if left[-1] > right[-1]:
            cnt += 1
        return merge(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)  # 병합 정렬은 sorted 느낌의 정렬이므로(비파괴형이라 다시 받아서 덮어쓰기)
    print(f'#{tc} {arr[N // 2]} {cnt}')

#
#--------------------------------------------------------------------
# 교수님 방법 2(인덱스로 접근)
# def merge_sort(arr):
#     global cnt
#     if len(arr) == 1:  # 리스트 원소가 하나 남을 때
#         return arr
#     else:
#         m = len(arr) // 2
#         left = arr[:m]  # 리스트 왼쪽 절반
#         right = arr[m:]  # 오른쪽 절반
#         left = merge_sort(left)  # 정렬된 리스트 리턴
#         right = merge_sort(right)  # 정렬된 리스트 리턴
#
#         left_idx = 0
#         right_idx = 0
#         i = 0
#         while left_idx < len(left) and right_idx < len(right):  # 좌우 리스트에서 비교 대상이 남은 경우
#             if left[left_idx] <= right[right_idx]:
#                 arr[i] = left[left_idx]
#                 left_idx += 1
#             else:
#                 arr[i] = right[right_idx]
#                 right_idx += 1
#             i += 1
#
#         if left_idx < len(left):  # 왼쪽 리스트가 남은 경우
#             arr[i:] = left[left_idx:]
#
#         if right_idx < len(right):  # 오른쪽 리스트가 남은 경우
#             arr[i:] = right[right_idx:]
#
#         #########################################################
#         if left[-1] > right[-1]:  # 왼쪽 마지막 원소가 큰 경우(문제)
#             cnt += 1
#         #########################################################
#
#         return arr  # 왼쪽 오른쪽을 합쳐 정렬된 리스트 반환
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     cnt = 0
#     arr = merge_sort(arr)
#     print('#{} {} {}'.format(tc + 1, arr[N // 2], cnt))