import sys
sys.stdin = open('D11768.txt')

from collections import deque

def merge(left, right):
    left = deque(left)
    right - deque(right)
    result = []

    # 둘 다 남았을 때
    while left and right:
        if left[0] < right[0]:
            result.append(left.popleft())
        else:
            result.append(right.popleft())

    # 이때 연산 단축
    # 왼쪽만 남았을 때
    if left:
        result += left # extend
    # 오른쪽만 남았을 때
    elif right:
        result.extend(right)

    return result


def merge_sort(a):
    global cnt
    if len(a) == 1:
        return a

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