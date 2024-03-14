def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            answer += 1
            dfs(n, computers, visited, i)
    return answer

def dfs(n, computers, visited, index):
    # 왔으면 방문 체크 해야지~
    visited[index] = 1
    for i in range(n):
        # 자기가 자기와 연결된 것 제외하고 다른 컴퓨터와 연결되었다면
        if i != index and computers[index][i] == 1 and visited[i] == 0:
            dfs(n, computers, visited, i)




#-------------
def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            answer += 1
            bfs(n, computers, visited, i)
    return answer

def bfs(n, computers, visited, index):
    # 왔으면 방문 체크 해야지~
    visited[index] = 1
    Q = [index]

    while Q:
        index = Q.pop(0)
        for i in range(n):
            # 자기가 자기와 연결된 것 제외하고 다른 컴퓨터와 연결되었다면
            if i != index and computers[index][i] == 1 and visited[i] == 0:
                visited[i] = 1
                Q.append(i)


