# 0 : 양, 1 : 늑대
# [부모 노드 번호, 자식 노드 번호]
def dfs(visited, info, edges, sheep, wolf):
    global answer
    if (sheep > wolf):
        answer = max(answer, sheep)
    else:
        return
    for p, c in edges:
        # 부모를 거쳐왔고 이전에 방문 안한 자식 노드가 있다면?
        if visited[p] == True and visited[c] == False:
            visited[c] = True
            # 양이면
            if info[c] == 0:
                dfs(visited, info, edges, sheep + 1, wolf)
            else:
                dfs(visited, info, edges, sheep, wolf + 1)
            visited[c] = False



def solution(info, edges):
    global answer
    answer = 0
    N = len(info)
    visited = [False] * N

    visited[0] = True
    dfs(visited, info, edges, 1, 0)

    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))