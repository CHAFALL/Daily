import sys
sys.stdin = open('D1248.txt')
# 서브 트리의 크기 구하기
def preorder(node):
    global cnt
    if node:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])

# 조상 구하기
def ancestor(node):
    res = [] # 조상 담을 곳
    while node:
        node = tree[node][2]  # 부모로 찾아 올라가기
        res.append(node)
    return res  # 이렇게 하면 마지막에 항상 0이 들어감

T = int(input())
for tc in range(1, T+1):
    V, E, A, B = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(V+1)]
    # 왼 자식, 오 자식, 부모
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

    # 가까운 공통조상 구하기
    ancestor_A = ancestor(A)
    ancestor_B = ancestor(B)
    # print(ancestor_A, ancestor_B)
    for a in ancestor_A:
        if a in ancestor_B:
            common_ancestor = a
            break

    preorder(common_ancestor)
    print(f'#{tc} {common_ancestor} {cnt}')