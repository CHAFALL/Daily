# 중위순회
def inorder(node):
    global i
    if node < (2 ** K):
        inorder(2 * node)
        tree[node] = temp[i]
        i += 1
        inorder(2 * node + 1)

K = int(input())
temp = list(map(int, input().split()))
tree = [0] * (2 ** K)

i = 0
inorder(1)

for i in range(K):
    for j in range(2 ** i, 2 ** (i+1)):
        print(tree[j], end=' ')
    print()