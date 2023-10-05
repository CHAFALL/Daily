# # Quene 1
# def enQ(data):
#     global rear
#     if rear == Qsize -1:     # 가득 차면
#         print('Q is Full')
#     else:
#         rear += 1
#         Q[rear] = data
#
#
# def deQ():
#     global front
#     if front == rear:  # 비어있으면..
#         print('큐가 비어있음')
#         return -1
#     else:
#         front += 1
#         return Q[front]
#
#
# Qsize = 3
# Q = [0] * 3
# rear = -1
# front = -1
#
# enQ(1)
# enQ(2)
# rear += 1 # enqueue(3)
# Q[rear] = 3
#
# # # 꺼낼 때는 미리 검사를 하고 꺼내는 방식을 많이 사용한다.
# # while front != rear: # 큐가 비어있지 않으면
# #     front += 1
# #     print(Q[front])
#
# print(deQ())
# print(deQ())
# front += 1
# temp = Q[front]
# print(temp)
#
#---------------------------------------------------------------------------
# append, pop 방식

# Q = []
#
# Q.append(1)    # enquene(1)
# Q.append(2)
# Q.append(3)
# print(Q.pop(0))
# print(Q.pop(0))
# print(Q.pop(0))
#-------------------------------------------------------------------
# 원형 큐 (얘도 꽉 차는 것은 어쩔 수 없다..., 이따가 알려주면 넣을래 아니면 덮어쓸래?)
# 상황에 맞게.. 쓸 것, 예를 들어 4시간 전의 날씨만 알면 된다면 덮어쓰기라든가.
# 미완...
def enq(data):
    global rear, front
    if (rear+1) % cQsize == front:
        front = (front+1) % cQsize
    rear = (rear+1) % cQsize
    cQ[rear] = data

def deq():
    global front
    front = (front+1) % cQsize
    return  cQ[front]

cQsize = 4
cQ = [0] * cQsize
front = 0
rear = 0

enq(1)
enq(2)
enq(3)
enq(4)
enq(5)
print(deq())
print(deq())
print(deq())
print(deq())
#--------------------------------------------------------------------------
# 덱(참고용)(내부적으로 매우 빠르게 동작가능)
# from collections import deque
#
# q = deque()
# q.append(1)
# q.append(2)
# q.append(3)
# print(q.popleft())
# print(q.popleft())
# print(q.popleft())




