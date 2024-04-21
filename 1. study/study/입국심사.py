# 이분 탐색 문제로 해당 시간에 몇 명을 쳐냈는지를 활용하는 문제

def solution(n, times):

    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2

        cnt = 0
        for time in times:
            cnt += mid // time
            # 만약에 이미 충분하다면?
            if cnt >= n:
                break

        # 과분할 경우 더 적은 시간일 때로
        if cnt >= n:
            right = mid - 1
        # 더 많은 시간이 필요할 경우
        elif cnt < n:
            left = mid + 1

    return right + 1

print(solution(6, [7, 10]))





#----
# 회의실 배정인가 강의실 배정 중 하나랑 비슷한 문제같음
# heapq로 더 적은 시간이 앞으로 가게 하고
# 맨 앞의 놈이 빌때까지 기다리는 식으로 풀면 될 듯

# 힙을 사용한 이유, 가장 최소값이 맨 앞으로 오므로
# 강의가 가장 빨리 끝나는 강의실을 구하기 용이

import heapq
N = int(input())
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append((s, e))

arr.sort()

room = []
heapq.heappush(room, arr[0][1])

for i in range(1, N):
    # 다음으로 빨리 시작하는 강의가
    # 가장 빨리 끝나는 강의시간보다 더 빨리 시작해야 한다면? 방 하나 더 만들기
    if arr[i][0] < room[0]:
        heapq.heappush(room, arr[i][1])
    # 반대라면? 그 강의 끝나면 그 방 써.
    else:
        heapq.heappop(room)
        heapq.heappush(room, arr[i][1])

# 자동으로 방이 쌓이게 될 것.
print(len(room))