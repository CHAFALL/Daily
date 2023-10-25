import sys
sys.stdin = open('D11927.txt')
# 이진 탐색 -> 중위순회 이용
def inorder(node):
    global num
    if node <= N:
        inorder(2 * node)
        tree[node] = num
        num += 1
        inorder(2 * node + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N + 1)
    num = 1

    inorder(1)
    print(f'#{tc} {tree[1]} {tree[N // 2]}')