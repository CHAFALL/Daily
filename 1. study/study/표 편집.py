# C++에서 배운 연결 리스트 써주면 되겠는데???

class Node:

    # 이전 노드와 다음 노드 여부 판단
    def __init__(self, p, n):
        self.prev = p
        self.next = n
        self.is_save = True


# n : 행 개수 , k : 처음에 선택된 행의 위치, cmd : 수행한 명령어 문자열 배열
def solution(n, k, cmd):

    # linked_list 초기화
    linked_list = {i: Node(i - 1, i + 1) for i in range(1, n + 1)}
    linked_list[1].prev = None  # 첫 번째 노드의 이전 노드는 없음
    linked_list[n].next = None  # 마지막 노드의 다음 노드는 없음

    now = k + 1

    # 삭제된 번호 담을 stack
    stack = []

    for cd in cmd:
        # 삭제
        if cd[0] == "C":
            # 비활성
            linked_list[now].is_save = False
            stack.append(now)

            prev, next = linked_list[now].prev, linked_list[now].next

            # [none][prev][node][next][none]

            if prev is not None:
                linked_list[prev].next = next

            if next is not None:
                linked_list[next].prev = prev

            # 만약에 다음 노드가 없다면 이전 노드 선택.
            # 아니라면 그대로 진행.
            if linked_list[now].next is None:
                now = linked_list[now].prev
            else:
                now = linked_list[now].next

        # 복구
        elif cd[0] == "Z":
            # 활성
            re = stack.pop()
            linked_list[re].is_save = True

            prev, next = linked_list[re].prev, linked_list[re].next

            # [none][prev][node][next][none]

            if prev is not None:
                linked_list[prev].next = re

            if next is not None:
                linked_list[next].prev = re

        else:
            type, cnt = cd.split()
            # 위
            if type == "U":
                for _ in range(int(cnt)):
                    now = linked_list[now].prev

            # 아래
            else:
                for _ in range(int(cnt)):
                    now = linked_list[now].next



    return ''.join('O' if linked_list[i].is_save else 'X' for i in range(1, n + 1))

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
