def enq(n): # 들어갈 원소
    global last
    # 1.완전 이진 트리 형태 유지
    last += 1
    heap[last] = n
    # 2.절대값 힙 조건 충족
    c = last
    p = c // 2

    while p and abs(heap[p]) > abs(heap[c]): # 조건 불충족하면 할 때까지
        heap[p], heap[c] = heap[c], heap[p]
        c = p // 2
        p = c // 2

    if abs(heap[p]) == abs(heap[c]):
        heap[p] = min(heap[p], heap[c])
        heap[c] = max(heap[p], heap[c])

def deq():
    global last
    tmp = heap[1] # 루트 백업
    heap[1] = heap[last] # 삭제할 노드의 키를 루트에 복사
    last -= 1 # 마지막 노드 삭제
    p = 1
    c = p * 2
    while c <= last:  # 자식이 하나라도 있으면...(오른쪽 자식도 체크)
        if c + 1 <= last and heap[c] < heap[c + 1]:  # 오른쪽 자식이 있고, 오른쪽 자식이 더 크면,
                                                     # 왼쪽 자식(c) + 1 하면 오른쪽 자식 됨
            c += 1  # 비교 대상이 오른쪽 자식노드
        if heap[p] > heap[c]:  # 자식이 더 크면 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p = c  # 자식을 새로운 부모로
            c = p * 2  # 왼쪽 자식 번호를 계산
        else:  # 부모가 더 크면
            break  # 비교 중단,

    return tmp


N = int(input())
heap = [0] * (N + 1)
last = 0
for _ in range(N):
    temp = int(input())
    if temp != 0:
        enq(temp)
    else:
        print(deq())
    