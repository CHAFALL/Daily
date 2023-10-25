import sys
sys.stdin = open('D11926.txt')

def preorder(node):
    global cnt
    if node:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    V = E + 1
    arr = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(V + 1)]
    # [왼자식, 오자식, 부모]
    for i in range(E):
        p, c = arr[2 * i], arr[2 * i + 1]
        # 부모를 통해 자식 구하기
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
        # 자식을 통해 부모 구하기
        tree[c][2] = p
    cnt = 0
    preorder(N)
    print(f'#{tc} {cnt}')