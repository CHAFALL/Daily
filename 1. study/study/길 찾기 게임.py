from sys import setrecursionlimit
setrecursionlimit(10000)

class Node:
    def __init__(self, info):
        self.num = info[2]  # 노드 번호
        self.x = info[0]  # x 좌표
        self.left = None  # 왼쪽 자식
        self.right = None  # 오른쪽 자식

# 핵심!!! 이진트리이다!!! -> y 좌표 check할 필요 없음. (sort를 해줘서)
def make_node(parent, info):
    # 부모의 x 좌표보다 작다면? -> 왼쪽
    if info[0] < parent.x:
        # 자식이 있다면?
        if parent.left:
            # 그 자식에 대해서 다시 가능성 보기
            make_node(parent.left, info)
        # 없다면 그 자리 차지
        else:
            parent.left = Node(info)

    else:
        if parent.right:
            make_node(parent.right, info)
        else:
            parent.right = Node(info)

# 전위 순회
def pre_order(node, result):
    if node:
        result.append(node.num) # 현재 노드 번호 추가
        pre_order(node.left, result)
        pre_order(node.right, result)

# 후위 순회
def post_order(node, result):
    if node:
        post_order(node.left, result)
        post_order(node.right, result)
        result.append(node.num) # 현재 노드 번호 추가

def solution(nodeinfo):
    answer = []

    N = len(nodeinfo)

    # sort를 위해 노드(인덱스) 정보 추가해주기
    for i, node in enumerate(nodeinfo):
        node.append(i + 1)

    # y좌표는 내림차순, x좌표는 오름차순
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))

    # 초기 설정
    tree = Node(nodeinfo[0])

    for i in range(1, N):
        make_node(tree, nodeinfo[i])

    # 전위 순회
    pre_result = []
    pre_order(tree, pre_result)
    answer.append(pre_result)

    # 후위 순회
    post_result = []
    post_order(tree, post_result)
    answer.append(post_result)

    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))

