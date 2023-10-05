# 인접 행렬 버전
# 장점: 구현이 쉽다.
# 단점: 메모리 낭비 (0도 표시를 하기 때문에)
# graph = [
#     [0, 1, 0, 1, 0],
#     [1, 0, 1, 1, 1],
#     [0, 1, 0, 0, 0],
#     [1, 1, 0, 0, 1],
#     [0, 1, 0, 1, 0]
# ]
#
# # DFS
# # stack 버전
# def dfs_stack(start):
#     visited = []
#     stack = [start]
#
#     while stack:
#         now = stack.pop()
#         # 이미 방문한 지점이라면 continue
#         if now in visited:
#             continue
#
#         # 방문하지 않은 지점이라면, 방문 표시
#         visited.append(now)
#
#         # 갈 수 있는 곳들을 stack에 추가
#         # for next in range(5):
#         # 작은 번호 부터 조회할려면??(아래)
#         for next in range(4, -1, -1):
#             # 연결이 안되어 있다면 continue
#             if graph[now][next] == 0:
#                 continue
#
#             # 방문한 지점이라면 stack에 추가하지 않음
#             if next in visited:
#                 continue
#
#             stack.append(next)
#
#     # 출력을 위한 반환
#     return visited
#
# print("dfs stack = ", end='')
# print(*dfs_stack(0)) # 0 3 4 1 2 (큰 숫자 먼저 가네?)

# TIP: 반복이나 재귀 같은 것을 만들 때 할 수 없는 것들을 위주로 구현하는 편
# 왜냐? 조건이 만족한다면으로 들어가면 and and and로 조건이 많이 붙어서 코드 복잡
# (개인적인 노하우임)


# # 재귀
# # MAP 크기(길이)를 알 때 append 형식 말고 아래와 같이 사용하면 훨씬 빠름
# visited = [0] * 5
# path = [] # 방문 순서 기록
#
# def dfs(now):
#     visited[now] = 1 # 현재 지점 방문 표시
#     # print(now, end=' ')
#     path.append(now)
#
#     # 인접한 노드들을 방문
#     for next in range(5):
#         # 연결이 안되어 있다면 continue
#         if graph[now][next] == 0:
#             continue
#
#         if visited[next]:
#             continue
#
#         dfs(next)
#
# print("dfs 재귀 = ", end='')
# dfs(0)
# print(*path)

#-------------------------------------------------------------------------------
#BFS
#
# graph = [
#     [0, 1, 0, 1, 0],
#     [1, 0, 1, 1, 1],
#     [0, 1, 0, 0, 0],
#     [1, 1, 0, 0, 1],
#     [0, 1, 0, 1, 0]
# ]
#
# def bfs(start):
#     visited = [0] * 5
#
#     # 먼저 방문 했던 것을 먼저 처리해야 한다.
#     queue = [start]
#     visited[start] = 1
#
#     while queue:
#         now = queue.pop(0)
#         print(now, end=' ')
#
#         # 방문 체크 + 방문한 지점은 pass
#
#         # 인접한 노드들을 queue에 추가
#         for next in range(5):
#             # 연결이 안 되어 있다면 continue
#             if graph[now][next] == 0:
#                 continue
#             # 방문한 지점이라면 queue에 추가하지 않음
#             if visited[next]:
#                 continue
#
#             queue.append(next)
#             # bfs 이므로 여기서 방문 체크를 해주어도 상관없다.
#             visited[next] = 1
# bfs(0)

#----------------------------------------------------------------------------
# 인접 리스트 버전
# 갈 수 있는 지점만 저장하자
# 주의사항
# -각 노드마다 갈 수 있는 지점의 개수가 다름
#     -> range 쓸 때 index 조심
# 메모리적으로 인접 행렬에 비해 훨씬 효율적이다.

graph = [
    [1, 3],
    [0, 2, 3, 4],
    [1],
    [0, 1, 4],
    [1, 3]
]

# 딕셔너리로도 가능함(파이썬 한정)
# graph_dict = {
#     '0': [1, 3],
#     '1': [0, 2, 3, 4],
#     '2': [1],
#     '3': [0, 1, 4],
#     '4': [1, 3]
# }

# DFS
# stack 버전
def dfs_stack(start):
    visited = []
    stack = [start]

    while stack:
        now = stack.pop()
        # 이미 방문한 지점이라면 continue
        if now in visited:
            continue

        # 방문하지 않은 지점이라면, 방문 표시
        visited.append(now)

        # 작은 번호 부터 조회할려면??(아래)
        for to in range(len(graph[now]) - 1, -1, -1):  # 여기 부분 바뀜
            # 이제 연결이 안되어있다는 건 애초에 저장하지 않았으므로
            # 아래도 체크할 필요 없음(연산 속도도 증가하겠네)
            # if graph[now][next] == 0:
            #     continue

            next = graph[now][to] # 여기도 추가 됨
            # next와 인덱스가 다르기 때문에 이렇게 해줘야 됨

            # 방문한 지점이라면 stack에 추가하지 않음
            if next in visited:
                continue

            stack.append(next)

    # 출력을 위한 반환
    return visited

print("dfs stack = ", end='')
print(*dfs_stack(0)) # 0 3 4 1 2 (큰 숫자 먼저 가네?)



# 재귀
# MAP 크기(길이)를 알 때 append 형식 말고 아래와 같이 사용하면 훨씬 빠름
visited = [0] * 5
path = [] # 방문 순서 기록

def dfs(now):
    visited[now] = 1 # 현재 지점 방문 표시
    # print(now, end=' ')
    path.append(now)

    # 인접한 노드들을 방문
    for to in range(len(graph[now])):
        # 이제 연결이 안되어있다는 건 애초에 저장하지 않았으므로
        # 아래도 체크할 필요 없음(연산 속도도 증가하겠네)
        # if graph[now][next] == 0:
        #     continue

        next = graph[now][to]  # 여기도 추가 됨
        # next와 인덱스가 다르기 때문에 이렇게 해줘야 됨

        if visited[next]:
            continue

        dfs(next)

print("dfs 재귀 = ", end='')
dfs(0)
print(*path)