import sys
sys.stdin = open('D11933.txt')

# 완전 이진 트리 특성 이용
# 나머지 채워주기 위함
def postorder(node, N):
    if node <= N:
        postorder(node * 2, N)
        postorder(node * 2 + 1, N)
        # 여기 아래부분 기억하기!!!
        if node * 2 + 1 <= N:  # 오른쪽 체크 (오른쪽 먼저 안하면 왼쪽만 계속 올라감)
            tree[node] = tree[node * 2] + tree[node * 2 + 1]
        elif node * 2 <= N:  # 왼쪽 체크
            tree[node] = tree[node * 2]


T = int(input())
for tc in range(1, T+1):
    # N 노드의 개수, M 리프 노드의 개수, L 출력할 노드 번호
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    # 잎만 트리에 넣어준 상태
    for _ in range(M):
        idx, num = map(int, input().split())
        tree[idx] = num

    postorder(1, N)

    print(f'#{tc} {tree[L]}')

