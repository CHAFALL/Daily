import heapq

def solution(operations):
    answer = []
    min_q = []
    max_q = []
    for op in operations:
        command, data = op.split()
        if command == "I":
            data = int(data)
            heapq.heappush(min_q, data)
            heapq.heappush(max_q, (-data, data))
        elif command == "D" and min_q:
            # 최소힙을 통해 최소값을 구하고 최소값을 최대힙에서 삭제
            if data == "-1":
                min_value = heapq.heappop(min_q)
                max_q.remove((-min_value, min_value))
            elif data == "1":
                max_value = heapq.heappop(max_q)[1]
                min_q.remove(max_value)

    if min_q:
        answer = [heapq.heappop(max_q)[1], heapq.heappop(min_q)]
    else:
        answer = [0, 0]

    return answer
