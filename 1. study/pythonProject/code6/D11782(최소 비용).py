import sys
sys.stdin = open('D11782.txt')

#
# # 누적 느낌이라(다익스트라)
# def dijkstra(i, j):
#     # 시작점 설정
#     D[i][j] = 0
#
#     for _ in range(N * N):
#         # 가중치 최소값 찾기
#         min_v = 987654321
#         for i in range(N):
#             for j in range(N):
#                 if min_v > D[i][j] and not visited[i][j]:
#                     min_v = D[i][j]
#                     # 너가 젤 작구나? 당첨
#                     vi, vj = i, j
#         # 방문체크
#         visited[vi][vj] = 1
#
#         # 갈 수 있는 방향 중에서 탐색
#         for k in range(4):
#             ni = vi + di[k]
#             nj = vj + dj[k]
#
#             if 0 <= ni < N and 0 <= nj < N\
#                     and not visited[ni][nj]:
#                 # 갈려는 곳의 높이가 기존보다 높다면?
#                 gap = 0
#                 if arr[ni][nj] > arr[vi][vj]:
#                     gap = arr[ni][nj] - arr[vi][vj]
#
#                 if D[ni][nj] > D[vi][vj] + gap + 1:
#                     D[ni][nj] = D[vi][vj] + gap + 1
#
#     return
#
#
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     D = [[987654321] * N for _ in range(N)]
#
#     dijkstra(0, 0)
#     print(f'#{tc} {D[N-1][N-1]}')
#-------------------------------------------------------------
# 다른 풀이
# import heapq
#
# def dijkstra(i, j):
#     pq = []
#     heapq.heappush(pq, (0, i, j)) # 가중치, 좌표
#     D[i][j] = 0
#     while pq:
#         # 가중치 최소값 찾기
#         d, vi, vj = heapq.heappop(pq)
#         visited[vi][vj] = 1
#
#         # 갈 수 있는 방향 중에서 탐색
#         for k in range(4):
#             ni = vi + di[k]
#             nj = vj + dj[k]
#
#             if 0 <= ni < N and 0 <= nj < N\
#                     and not visited[ni][nj]:
#                 # 갈려는 곳의 높이가 기존보다 높다면?
#                 gap = 0
#                 if arr[ni][nj] > arr[vi][vj]:
#                     gap = arr[ni][nj] - arr[vi][vj]
#
#                 if D[ni][nj] > D[vi][vj] + gap + 1:
#                     D[ni][nj] = D[vi][vj] + gap + 1
#                     heapq.heappush(pq, (D[ni][nj], ni, nj))
#     return
#
#
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0] * N for _ in range(N)]
#     D = [[987654321] * N for _ in range(N)]
#
#     dijkstra(0, 0)
#     print(f'#{tc} {D[N-1][N-1]}')

#----------------------------------------------------------------
# 다익스트라는 경로를 알 수 없다.(여러 경우의 수로 같은 비용인 것이 있다.)
# 교수님 풀이

# def dijkstra(x, y):
#     # 1. 시작점 설정
#     D[x][y] = 0
#     # 2. 정점갯수 반복(N * N)
#     for _ in range(N * N):  # while로 해도 됨(어차피 나올꺼라)
#         # 2-1가중치 최소값 찾기
#         min_v = INF
#         for i in range(N):
#             for j in range(N):
#                 if not visited[i][j] and min_v > D[i][j]  :
#                     min_v = D[i][j]
#                     # 너가 젤 작구나? 당첨
#                     x, y = i, j # cx, cy 로도 좀 쓰임
#
#         # 2-2 방문체크 + 할일
#         visited[x][y] = 1
#         if x == N-1 and y == N-1: return  # while 가능한 이유
#
#         # 2-3. 인접 정점(4)의 가중치 갱신
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#
#             # 인접하고 방문 안한 정점
#             if 0 <= nx < N and 0 <= ny < N\
#                     and not visited[nx][ny]:
#                 # 갈려는 곳의 높이가 기존보다 높다면?
#                 diff = 0  # 경사도
#                 if arr[nx][ny] > arr[x][y]:
#                     diff = arr[nx][ny] - arr[x][y]
#                 # 업데이트
#                 if D[nx][ny] > D[x][y] + diff + 1:
#                     D[nx][ny] = D[x][y] + diff + 1
#
#     return
#
#
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
#
# INF = 987654321
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)] # 경사도 행렬
#     visited = [[0] * N for _ in range(N)]  # 방문체크
#     D = [[INF] * N for _ in range(N)]  # 가중치
#
#     dijkstra(0, 0)
#     print(f'#{tc} {D[N-1][N-1]}')
#---------------------------------------
# 교수님 방법 2
import heapq


def dijkstra(x, y):
    # 1. 시작점 설정
    heap = []
    D[x][y] = 0
    heapq.heappush(heap, (D[x][y], x, y))  # 가중치, x ,y
    # 2. 정점갯수 반복(N * N)
    while heap:  # for으로 하면 안됨(찾아보기)
        # for _ in range(N * N):  # while로 해도 됨(어차피 나올꺼라)
        #     # 2-1가중치 최소값 찾기
        #     min_v = INF
        #     for i in range(N):
        #         for j in range(N):
        #             if not visited[i][j] and min_v > D[i][j]  :
        #                 min_v = D[i][j]
        #                 # 너가 젤 작구나? 당첨
        #                 x, y = i, j # cx, cy 로도 좀 쓰임
        d, x, y = heapq.heappop(heap)
        # 2-2 방문체크 + 할일
        visited[x][y] = 1  # 넣을 때 해도 되고 빠질 때 해도 됨
        if x == N - 1 and y == N - 1: return  # while 가능한 이유

        # 2-3. 인접 정점(4)의 가중치 갱신
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 인접하고 방문 안한 정점
            if 0 <= nx < N and 0 <= ny < N \
                    and not visited[nx][ny]:
                # 갈려는 곳의 높이가 기존보다 높다면?
                diff = 0  # 경사도
                if arr[nx][ny] > arr[x][y]:
                    diff = arr[nx][ny] - arr[x][y]
                # 업데이트
                if D[nx][ny] > D[x][y] + diff + 1:
                    D[nx][ny] = D[x][y] + diff + 1
                    heapq.heappush(heap, (D[nx][ny], nx, ny))

    return


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

INF = 987654321
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]  # 경사도 행렬
    visited = [[0] * N for _ in range(N)]  # 방문체크
    D = [[INF] * N for _ in range(N)]  # 가중치

    dijkstra(0, 0)
    print(f'#{tc} {D[N - 1][N - 1]}')
