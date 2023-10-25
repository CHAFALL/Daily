#heapq (힙 큐 알고리즘)
# 최소합만 지원
import heapq
heap = [7, 2, 5, 3, 4, 6]
heapq.heapify(heap)
print(heap) # [2, 3, 5, 7, 4, 6]
heapq.heappush(heap, 1)
print(heap) # [1, 3, 2, 7, 4, 6, 5]
while heap:
    print(heapq.heappop(heap), end=' ')
print()
########################################################
# 최대힙은?
temp = [7, 2, 5, 3, 4, 6]
heap2 = []
for i in range(len(temp)):
    heapq.heappush(heap2, -temp[i])
print(heap2) #[-7, -4, -6, -2, -3, -5] # 뽑을 때 음수 달면 됨
heapq.heappush(heap2, -1)
print(heap2) #[-7, -4, -6, -2, -3, -5, -1]
while heap2:
    print(heapq.heappop(heap2) * -1, end= ' ') # 7 6 5 4 3 2 1