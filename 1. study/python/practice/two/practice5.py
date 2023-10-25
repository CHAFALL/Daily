# 선형큐 front rear 사용
# Quene는 초기 크기를 크게 잡아야 한다.
# SIZE = 100
# Q = [0] * SIZE
# front = rear = -1
#
# # enQuene
# rear += 1
# Q[rear] = 1
# rear += 1
# Q[rear] = 2
# rear += 1
# Q[rear] = 3
#
# # peek
# print(f'peek : {Q[front+1]}')
#
# #deQuene
# while front != rear:
#     front += 1
#     print(Q[front]) #1
#                     #2
#                     #3
#
# print(front, rear) # 2 2
# print(Q)
#-------------------------------------------------------------------
# #선형큐 리스트, 메소드 사용
# Q = []
#
# # enQ
# Q.append(1)
# Q.append(2)
# Q.append(3)
#
# #peek
# print(f'peek : {Q[0]}') # peek : 1
# #deQ
# while Q:
#     print(Q.pop(0)) # O(n)임 O(1)이 아니라 시간 쬐매 걸림
#     # 1
#     # 2
#     # 3

#-----------------------------------------------------------------
# 선형큐(deque 사용)(pop(0)사용이 많아서 속도가 느릴 때 이용)
from collections import deque

Q = deque()

# enQ
Q.append(1)
Q.append(2)
Q.append(3)

#peek
print(f'peek : {Q[0]}')
#deQ
while Q:
    print(Q.popleft())