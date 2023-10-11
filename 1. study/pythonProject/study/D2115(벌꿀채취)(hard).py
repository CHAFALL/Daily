import sys
sys.stdin = open('D2115.txt')

def dfs(k, i, j, honey, cost): # 깊이(연속으로 M개를 표현하기 위해), 좌표, 꿀의 양, 비용
    global max_v
    if honey > C: # 채취할 수 있는 꿀의 양 초과한 경우
        return
    if k == M:
        max_v = max(max_v, cost)
        return
    else:
        # 현재 벌통을 고를 경우
        dfs(k + 1, i, j, honey + arr[i][j+k], cost + arr[i][j+k] ** 2)
        # 현재 벌통을 고르지 않는 경우
        dfs(k + 1, i, j, honey, cost)

T = int(input())
for tc in range(1, T + 1):
    # 벌통들의 크기, 선택할 수 있는 벌통의 개수, 꿀을 채취할 수 있는 최대 양
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # 각각 벌통을 선택하는 경우 구현
    for i1 in range(N):
        for j1 in range(N - M + 1):
            max_v = 0
            dfs(0, i1, j1, 0, 0)
            cost1 = max_v  # 일꾼 1의 값
            for i2 in range(i1, N):
                # 겹치지 않도록 하기 위해
                sj = 0
                if i1 == i2: # 같은 줄이라면
                   sj = j1 + M
                for j2 in range(sj, N - M + 1):
                    max_v = 0
                    dfs(0, i2, j2, 0, 0)
                    cost2 = max_v # 일꾼 2의 값
                    ans = max(ans, cost1 + cost2)
    print(f'#{tc} {ans}')





