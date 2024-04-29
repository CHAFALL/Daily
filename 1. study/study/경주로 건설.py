# 일단 방문체크가 있어야 될까? 딴 길로 왔는데 더 빠른 루트였다면?
# 다른 느낌의 방문체크가 있어야 될 듯
# 방향 전환 오랜만에 ㄱ?
# BFS?

from collections import deque

# 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(board):
    N = len(board)
    # 방문 시에 비용이 얼마나 들었나 체크할 배열
    # 같을 시에도 갱신해줄 것!! (그래야 멈추지 않고 계속 진행)
    cost = [[987654321] * N for _ in range(N)]
    # 시작 지점
    cost[0][0] = 0

    Q = deque()
    # 방향을 9로 한 이유는 시각지점에서 오른쪽과 아래쪽 둘 다 드는 비용이 100으로 고정하기 위함
    Q.append((0, 0, 0, 9))  # 좌표 i, j, 비용, 방향

    while Q:
        i, j, c, dir = Q.popleft()

        if i == N - 1 and j == N - 1:
            # 더 나은 루트가 있을 수 있으므로 바로 나오지 않음
            continue

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            # 인덱스 조건
            if 0 <= ni < N and 0 <= nj < N:
                # 벽이면 다른 방향 찾기
                if board[ni][nj] == 1:
                    continue
                # 비용 관련
                # 만약에 첫 스타트거나 방향 변화가 없으면
                if dir == 9 or dir == k:
                    nc = c + 100
                else:
                    nc = c + 600

                # 비용이 작거나 같으면 갱신하고 Q에 넣어주기(넌 갈만한 애야)
                if nc <= cost[ni][nj]:
                    cost[ni][nj] = nc
                    Q.append((ni, nj, nc, k))

    return cost[N - 1][N - 1]


def solution(board):

    return bfs(board)

print(solution([[0, 0, 0, 0, 0],[0, 1, 1, 1, 0],[0, 0, 1, 0, 0],[1, 0, 0, 0, 1],[1, 1, 1, 0, 0]]))

# 이 문제는 단순히 그 위치에서의 최소 비용을 저장하면 안되고 그 위치에서 방향별 최소비용을 저장할 수 있도록 해야합니다.
# 방향이 비용에 영향을 끼치기 때문입니다.

#dfs는 한 경로를 끝까지 쭉 가보는 반면 bfs는 모든 경웅의 수에 대해서 depth를 하나씩 늘려가면서 진행하죠.
# 이 문제의 경우 현재까지의 코스트가 최소라고 해도
# 다음번에 꺾이느냐 안꺾이느냐에 따라서 최적 경로와 코스트가 달라지므로 기본적인 dfs 방법으로는 풀기 힘들겠네요.