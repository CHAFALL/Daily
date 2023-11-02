# 중위 순회 방식으로 트리 형성
def inorder(node):
    global i
    if node < (2 ** K):
        inorder(2 * node)
        tree[node] = temp[i]
        i += 1
        inorder(2 * node + 1)


K = int(input())
tree = [0] * (2 ** K)
temp = list(map(int, input().split()))
i = 0

inorder(1)

print(tree)

