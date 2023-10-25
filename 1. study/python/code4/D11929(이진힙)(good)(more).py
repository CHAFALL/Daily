import sys
sys.stdin = open('D11929.txt')
# 최소힙 삽입
def enq(n): # 들어갈 원소
    global last
    # 1.완전이진트리 형태 유지
    last += 1
    heap[last] = n
    # 2. 최소힙(부모 < 자식) 조건 충족
    c = last
    p = c // 2

    while p and heap[p] > heap[c]: # 조건 불충족하면 할 때까지 반복
        heap[p], heap[c] = heap[c], heap[p]
        c = p  # 자식이 부모자리에 갔으므로
        p = c // 2

# 마지막 놈의 조상들 찾기
def find_ancestor():
    p = last // 2 # 5 // 2 = 2
    total = 0
    while p:
        total += heap[p]
        p //= 2
    return total


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (N + 1)
    last = 0

    for i in range(N):
        enq(arr[i])

    print(f'#{tc} {find_ancestor()}')