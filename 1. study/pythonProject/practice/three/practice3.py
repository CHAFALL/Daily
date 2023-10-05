# 재귀 함수 할 시 고려사항 4가지
# 기저 조건
# 들어가기 전 로직
# 다음 재귀 함수 호출
# 돌아와서 할 로직

# 대부분의 백트래킹 구조
#def func():
    # 재귀를 끝내는 기저 조건

    # 가지치기

    # 반복문
        # 가지치기

        # 재귀 들어가기 전
        # 재귀 함수 호출
        # 돌아와서 초기화


# # {1, 2, 3} 집합에서 3개의 숫자를 선택하는 기본적인 예제
#
# arr = [i for i in range(1, 4)]
# path = [0] * 3
# def backtracking(cnt):
#     # 기저 조건
#     # 숫자 3개를 골랐을 때 종료
#     if cnt == 3:
#         print(*path)
#         return
#
#     for num in arr:
#         # 들어가기 전 로직 - 경로 저장
#         path[cnt] = num
#         # 다음 재귀 함수 호출
#         backtracking(cnt + 1)
#         # 돌아와서 할 로직
#
# backtracking(0)
#--------------------------------------------------------------------
# 위의 예제에서 이미 사용한 숫자는 사용하지 않도록
# arr = [i for i in range(1, 4)]
# path = [0] * 3
# def backtracking(cnt):
#     # 기저 조건
#     # 숫자 3개를 골랐을 때 종료
#     if cnt == 3:
#         print(*path)
#         return
#
#     for num in arr:
#         # 가지치기 - 중복된 숫자 제거
#         # 조건을 작성하는 것이 핵심
#         if num in path:
#             continue
#
#         # 들어가기 전 로직 - 경로 저장
#         path[cnt] = num
#         # 다음 재귀 함수 호출
#         backtracking(cnt + 1)
#         # 돌아와서 할 로직
#         path[cnt] = 0  # 이전에 선택했던 상태가 남아있으면 안됨(초기화)
#
#         # 내 생각: 내가 연산자 끼워넣기 문제에서 초기화가 필요없었던 이유?
#         # 단비 누나꺼랑 비교하기
          # 깨달음: 매개변수로 연산자를 넣어놔서 괜찮음
#
# backtracking(0)
#-----------------------------------------------------------------------------------
# 이진 트리 저장

# 0. 이진 트리 저장
#   - 일차원 배열 저장
# 1. 연결 리스트로 저장 - 개발용
# class TreeNode:
#     def __init__(self, value):  # 인스턴스 데이터
#         self.value = value
#         self.left = None
#         self.right = None
#     # 삽입 함수
#     def insert(self, childNode):
#         # 왼쪽 자식이 없을 경우
#         if not self.left:
#             self.left = childNode
#             return
#         # 오른쪽 자식이 없을 경우
#         if not self.right:
#             self.right = childNode
#             return
#
#         return
#     # 순회
#     def preorder(self):
#         # 아무것도 없는 트리를 조회할 때
#         if self != None:
#             # 전위 순회
#             print(self.value, end=' ')
#
#             # 왼쪽이 있다면 왼쪽 자식 조회
#             if self.left:
#                 self.left.preorder()
#
#             # 중위 순회
#             # print(self.value, end=' ')
#
#             # 오른쪽이 있다면 오른쪽 자식 조회
#             if self.right:
#                 self.right.preorder()
#
#             # 후위 순회
#             # print(self.value, end=' ')
#
# arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]
# # 이진 트리 만들기
# nodes = [TreeNode(i) for i in range(0, 14)]
# for i in range(0, len(arr), 2):
#     parentNode = arr[i]
#     childNode = arr[i + 1]
#     nodes[parentNode].insert(nodes[childNode])
#
# nodes[1].preorder()

#-------------------------------------------------------------

# 2. 인접 리스트로 저장(각자가 갈 수 있는 경로만 저장)
# (인접행렬은 편하게 2차원 배열로 작성할 수 있는 장점이 있지만, 0을 다 저장\
# 해야 되어서 손해보는 부분이 many)
# (인접 리스트는 갈 수 있는 경로만 저장하기 때문에 메모리와 시간 효율적)

arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]


nodes = [[] for i in range(0, 14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i + 1]
    nodes[parentNode].append(childNode)

for i in range(len(nodes)):
    print(nodes[i])

# 자식이 더 이상 없다는 걸 표현하기 위해 None을 삽입
for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)

def preorder(nodeNumber):
    if nodeNumber == None:
        return
    print(nodeNumber, end=' ')
    preorder(nodes[nodeNumber][0])
    # print(nodeNumber, end=' ')
    preorder(nodes[nodeNumber][1])
    # print(nodeNumber, end=' ')
preorder(1)