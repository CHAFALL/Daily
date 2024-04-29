def can_cross(stones, k, mid):
    # mid 명이 건너려 할 때 연속으로 0이 되는 디딤돌의 최대 개수를 체크
    zeros = 0
    for stone in stones:
        if stone < mid:
            zeros += 1  # mid 명이면 0이 되는 디딤돌의 개수를 증가
        else:
            zeros = 0  # 0이 아닌 디딤돌을 만나면 리셋
        if zeros >= k:  # 연속된 k개의 디딤돌이 0이 되면 건널 수 없음
            return False
    return True

def solution(stones, k):
    left, right = 1, max(stones)  # 이진 탐색 범위 설정
    while left < right:
        mid = (left + right) // 2
        if can_cross(stones, k, mid):
            left = mid + 1  # 건널 수 있으면 인원 수를 늘림
        else:
            right = mid  # 건널 수 없으면 인원 수를 줄임
    return left - 1  # left가 건널 수 없는 최소 인원 수이므로, 건널 수 있는 최대 인원은 left - 1

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
print(solution([7, 2, 8, 7, 2, 5, 9], 3))