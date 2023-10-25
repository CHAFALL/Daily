# 그래프 순회
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# DFS
# def dfs(v):
#     visited[v] = 1
#     print(v, end=' ')
#     for w in adj_list[v]:  # 여기서 w는 인덱스가 아니라 정점이 됨
#         if visited[w] == 0:
#             dfs(w)
#
#
# V, E = map(int, input().split())
# temp = list(map(int, input().split()))
# adj_list = [[] for _ in range(V + 1)]  # 인접리스트 초기화
# visited = [0] * (V + 1)
#
# # 인접리스트 만들기
# for i in range(E):
#     s, e = temp[2 * i], temp[2 * i + 1]
#     adj_list[s].append(e)
#     adj_list[e].append(s)  # 무향일 때
#
# # print(adj_list) #[[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
# # 크기가 다 다름을 알 수 있다.(파이썬이라 가능)
# dfs(1)
#--------------------------------------------------------

def bfs(v):
    Q = [v]
    visited[v] = 1

    while Q:
        v = Q.pop(0) # 디큐
        # 하고 싶은 일 하기
        print(v, end=' ')
        for w in adj_list[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1




V, E = map(int, input().split())
temp = list(map(int, input().split()))
adj_list = [[] for _ in range(V + 1)]  # 인접리스트 초기화
visited = [0] * (V + 1)

# 인접리스트 만들기
for i in range(E):
    s, e = temp[2 * i], temp[2 * i + 1]
    adj_list[s].append(e)
    adj_list[e].append(s)  # 무향일 때

bfs(1)
print(visited)