# 최대한 평이하게 하는 것이 핵심!!
# 최대힙 쓰면 될 듯

import heapq

def solution(n, works):

    heap = []

    if sum(works) <= n:
        return 0

    for work in works:
        heapq.heappush(heap, -work)  # 최대힙

    # 작업량 만큼 젤 큰놈 1씩 손 봐주기
    for _ in range(n):
        work = heapq.heappop(heap) + 1 # 주의!! (최대힙 구현을 위해 음수로 되어있어서 - (- 1))
        heapq.heappush(heap, work)

    # 야근 피로도 구하기

    answer = 0
    for hp in heap:
        answer += hp ** 2

    return answer


print(solution(4, [4, 3, 3]))