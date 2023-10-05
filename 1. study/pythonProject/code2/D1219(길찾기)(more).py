import sys
sys.stdin = open('D1219.txt')
# def dfs(v):
#     visited[v] = 1
#     for w in range(100):
#         if visited[w] == 0 and adj[v][w] == 1:
#             dfs(w)
#
# T = 10
# for _ in range(1, T+1):
#     tc, E = map(int, input().split())
#     temp = list(map(int, input().split()))
#
#     # 초기설정
#     adj = [[0] * 100 for _ in range(100)]
#     visited = [0] * 100
#     # 인접행렬 만들기
#     for i in range(E):# 기억하도록
#         s, e = temp[i * 2], temp[i * 2 + 1]
#         adj[s][e] = 1
#
#     dfs(0)
#
#     print(f'#{tc} {visited[99]}')


#-----------------------------------------------------
#연습

def dfs(v):
    visited[v] = 1
    for w in range(100):
        if visited[w] == 0 and adj[v][w] == 1:
            dfs(w)


T = 10
for _ in range(1, T+1):
    tc, E = map(int, input().split())
    temp = list(map(int, input().split()))
    # 초기설정
    adj = [[0] * 100 for _ in range(100)]
    visited = [0] * 100
    # 인접행렬 만들기
    for i in range(E):
        s, e = temp[i * 2], temp[i * 2 + 1]
        adj[s][e] += 1

    dfs(0)

    print(visited[99])