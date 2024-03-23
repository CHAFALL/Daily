# 조상 구하기
def ancestor(node):
    res = [] # 조상 담을 곳
    while node:
				# 자신도 공통조상이 될 수가 있다????
        res.append(node)
        node = tree[node][2] # 부모를 찾아 올라가기
    return res


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tree = [[0] * 3 for _ in range(N + 1)]
    for _ in range(N - 1):
        p, c = map(int, input().split())

        # 부모를 통해 자식 구하기
        # 왼쪽 자식이 없다면 왼쪽에 넣고
        if tree[p][0] == 0:
            tree[p][0] = c
        # 있다면 오른쪽에 넣기
        else:
            tree[p][1] = c
        # 자식을 통해 부모 구하기
        tree[c][2] = p

    # 가장 가까운 공통 조상을 구할 두 노드
    A, B = map(int, input().split())

    # A와 B 조상들 구하기
    ancestor_A = ancestor(A)
    ancestor_B = ancestor(B)

    for target in ancestor_A:
        if target in ancestor_B:
            common_ancestor = target
            print(target)
            break

#---------------------------------------------------
# 조상 구하기
def ancestor(node):
    res = [] # 조상 담을 곳
    while node:
        res.append(node)
        node = tree[node]
    return res


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N + 1)
    for _ in range(N - 1):
        p, c = map(int, input().split())

        # 자식을 통해 부모 넣어주기
        tree[c] = p

    # 가장 가까운 공통 조상을 구할 두 노드
    A, B = map(int, input().split())

    # A와 B 조상들 구하기
    ancestor_A = ancestor(A)
    ancestor_B = ancestor(B)

    for target in ancestor_A:
        if target in ancestor_B:
            common_ancestor = target
            print(target)
            break