import sys
sys.stdin = open('D1231.txt')

# 완전 이진 트리 형식임을 이용
# 부모와 자식의 관계는 정해져 있으므로 일일히 안 만들어도 됨
def inorder(node, N):
    if node <= N: # 여기 주의
        inorder(2 * node, N)
        print(tree[node], end = '')
        inorder(2 * node + 1, N)

T = 10
for tc in range(1, T+1):
    N = int(input()) # 정점의 개수
    tree = [0] * (N+1)
    for _ in range(N):
        arr = input().split()
        # 정점의 순서가 뒤죽박죽일 때를 대비
        tree[int(arr[0])] = arr[1]

    print(f'#{tc} ', end='')
    inorder(1, N)
    print()