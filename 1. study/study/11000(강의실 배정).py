'''
3
1 3
2 4
3 5
'''
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
