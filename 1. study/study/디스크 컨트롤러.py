import heapq

def solution(jobs):
    answer = cnt = now = 0
    prev = -1

    N = len(jobs)
    Q = [] # 요청시간, 걸리는 시간

    while cnt < N:
        # 힙에 넣을 수 있는 조건:
        # 이전 것의 시작시각보다 크고 현재시각보다 시작시각이 작거나 같을 때
        for job in jobs:
            if prev < job[0] <= now:
                heapq.heappush(Q, (job[1], job[0])) # 걸리는 시간이 앞으로 가도록
        if Q:
            time, start_time = heapq.heappop(Q)
            prev = now # -> 이걸하는 이유 : 전에 했던 것이 또 들어가지 않게 하려고
            now += time # 걸린 시간만큼 현재시간 계산
            answer += now - start_time
            cnt += 1
        # 처리할 게 없으면 현재시간 + 1
        else:
            now += 1


    return int(answer / N)

print(solution([[0, 3], [1, 9], [2, 6]]))