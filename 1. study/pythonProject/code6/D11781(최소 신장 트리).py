import sys
sys.stdin = open('D11781.txt')

# def prim(s):
#     total = 0
#     # 시작점 설정
#     D[s] = 0
#     # 정점의 갯수만큼 선택하기
#     for i in range(V+1):
#
#         # 가중치 최소값 찾기
#         min_v = 987654321
#         for j in range(V+1):
#             if visited[j] == 0 and D[j] < min_v:
#                 min_v = D[j]
#                 v = j # 정점 선택
#         # 방문처리(선택)
#         visited[v] = 1
#         total += adj[PI[v]][v]
#         for w in range(V + 1):
#             if adj[v][w] and not visited[w]:
#                 if D[w] > adj[v][w]:
#                     D[w] = adj[v][w]
#                     PI[w] = v
#     return total
# # 노드 0부터 시작함
# T = int(input())
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())
#     adj = [[0] * (V+1) for _ in range(V + 1)]
#     visited = [0] * (V + 1)
#     D = [987654321] * (V + 1) # 가중치
#     PI = list(range(V + 1)) # 부모
#
#     # 인접행렬
#     for _ in range(E):
#         # 양 끝 노드 ,가중치
#         s, e, w = map(int, input().split())
#         adj[s][e] = adj[e][s] = w # 무향
#
#     # 간선의 가중치 합
#     print(f'#{tc} {prim(0)}')

#------------------------------------------------------------
#kruskal

# cf)이차 정렬이라면?, x[2]다음에 x[0] 순으로 정렬
    # edges.sort(key=lambda x: (x[2], x[0]))

def find_set(x):
    # while 문으로 만들 수도 있다.
    if P[x] == x:
        return x
    else:
        return find_set(P[x])



def kruskal():
    # 0. 초기화
    total = 0
    cnt = 0 # 간선의 갯수
    # 1. 간선의 배열 가중치 정렬
    edges.sort(key=lambda x:x[2])
    # 2. 간선을 "V"개 선택해야 한다.(정점의 갯수는 V + 1) (정점이 0 ~ V번)
    for i in range(E):
        # 각 정점의 find-set 비교
        p1 = find_set(edges[i][0])
        p2 = find_set(edges[i][1])
        if p1 != p2:
            # 2-1-1. union 및 할 일 하기
            P[p2] = p1  # union (p2의 부모는 p1이야)
            total += edges[i][2]  # 가중치
            cnt += 1 # 좀 더 공부 ㄱ
        if cnt == V:
            return total

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    P = list(range(V + 1))  # make-set
    print(f'#{tc} {kruskal()}')



