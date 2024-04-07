def solution(stones, k):

    # 초기 설정
    left = 1
    right = max(stones)


    while left <= right:
        cnt = 0
        mid = (left + right) // 2  # 테스트할 허용 인원수
        for stone in stones:
            if (stone - mid) <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break

        if cnt < k:
            left = mid + 1  # 허용 인원 증가
        else:
            right = mid - 1  # 허용 인원 감소



    return left




print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))


# 한 명씩 건너보면 안됨.
# 특정 x명이 건널 수 있는지 없는지 판단을 해야됨
# 동시에 올라가서 판단한다고 보면 됨.


# 내가 알때는 이진탐색은 정렬을 해야되는 것이었는데??

# 개 오래 걸릴 듯

# 만약 지금 건너려는 돌이 0이라면?
# 연속 여부 판단 (이전도 0이었으면 cnt + 1)
# 밟은 돌 -1 해줌