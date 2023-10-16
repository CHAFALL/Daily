def comb(k, p_list, s):  # s :시작번호
    global min_v

    if k == M:
        # 각 집마다 가성비 좋은 치킨 거리 찾기
        total = 0
        for hs in house:
            temp = 987654321
            for p in p_list:
                temp = min(temp, abs(hs[0] - p[0]) + abs(hs[1] - p[1]))
            total += temp
        min_v = min(min_v, total)
        return

    else:
        # 조합
        for i in range(s, C - M + 1 + k):
            comb(k + 1, p_list + [chicken[i]], i + 1)


# M : 폐업시키지 않을 치킨집
N, M = map(int, input().split())
# 0:빈칸. 1:집, 2:치킨집
arr = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []
for i in range(N):
    for j in range(N):
        # 집 좌표 넣어주기
        if arr[i][j] == 1:
            house.append((i, j))
        # 치킨 집 좌표 넣어주기
        elif arr[i][j] == 2:
            chicken.append((i, j))

min_v = 987654321
C = len(chicken)
comb(0, [], 0)
print(min_v)
