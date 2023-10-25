import sys
sys.stdin = open('D1238.txt')

# 강사님 풀이
# bfs 문제

# def bfs(s):
#     q = [s]
#     visited = [0] * 101
#     # 시작점은 방문 처리
#     visited[s] = 1
#     # 최대숫자와, 최대 깊이를 저장할 변수
#     max_number = s
#     max_depth = 1
#     while q:
#         now = q.pop(0)
#
#         # 갈 수 있는 지점 다 봐라
#         for to in graph[now]:
#             if visited[to]:
#                 continue
#
#             # 기존 방문보다 한 번 더 갔다.
#             visited[to] = visited[now] + 1
#             # 한 단계 깊은 곳으로 가거나
#             # 깊이는 같은데, 숫자가 더 크다면
#             # max 값을 초기화
#             if max_depth < visited[to] or\
#                     (max_depth == visited[to] and max_number < to):
#                 max_depth = visited[to]
#                 max_number = to
#
#             q.append(to)
#
#     return max_number
#
#
# T = 10
# for tc in range(1, T + 1):
#     n, start = map(int, input().split())
#     # 임시로 전체 입력을 받음
#     input_graph = list(map(int, input().split()))
#
#     # 인접리스트로 하는 것을 추천(0이 너무 많아서)
#     # 실제로 사용할 인접 리스트
#     graph = [[] for _ in range(101)]
#     for i in range(0, n, 2):
#         f, t = input_graph[i], input_graph[i + 1]
#         graph[f].append(t)
#
#     print(f'#{tc} {bfs(start)}')

#---------------------------------------------------------
# 다른 방식(내가 생각한 방식)
def bfs(s):
    q = [s]

    # 시작점은 방문 처리
    visited[s] = 1
    while q:
        now = q.pop(0)

        # 갈 수 있는 지점 다 봐라
        for to in graph[now]:
            if visited[to]:
                continue

            # 기존 방문보다 한 번 더 갔다.
            visited[to] = visited[now] + 1
            q.append(to)

    return


T = 10
for tc in range(1, T + 1):
    n, start = map(int, input().split())
    # 임시로 전체 입력을 받음
    input_graph = list(map(int, input().split()))
    visited = [0] * 101
    # 인접리스트로 하는 것을 추천(0이 너무 많아서)
    # 실제로 사용할 인접 리스트
    graph = [[] for _ in range(101)]
    for i in range(0, n, 2):
        f, t = input_graph[i], input_graph[i + 1]
        graph[f].append(t)

    bfs(start)

    # 가장 방문의 숫자가 큰 것에서 가장 큰 수 찾기
    # 뒤에서 부터 해서 바로 나오도록 함
    max_depth = max(visited)
    for i in range(100, -1, -1):
        if visited[i] == max_depth:
            print(f'#{tc} {i}')
            break



