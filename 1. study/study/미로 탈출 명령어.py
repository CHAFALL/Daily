import sys
sys.setrecursionlimit(10**5)

# d l r u 순으로
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
dir = ["d", "l", "r", "u"]

# 전역변수로 빼려고
_n = _m = _r = _c = _k = 0

def find_dist(x, y):
    return abs(x - _r) + abs (y - _c)

def dfs(x, y, path, cnt):
    # 종료조건
    if cnt == _k:
        if x == _r and y == _c:
            return path

    # 4방향 돌기
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 < nx <= _n and 0 < ny <= _m:
            dist = find_dist(nx, ny)

            # 가지치기
            if dist > _k - (cnt + 1):
                continue

            # 목표지점에 도달했을 경우 더 이상 탐색을 할 필요가 없으므로
            result = dfs(nx, ny, path + dir[k], cnt + 1)
            if result is not None:
                return result

    return None

def solution(n, m, x, y, r, c, k):

    # 함수 내에서 전역 변수 건들 때는 global 필요
    global _n, _m, _r, _c, _k
    _n, _m, _r, _c, _k = n, m, r, c, k

    dist = find_dist(x, y)

    # 최단 거리가 k보다 크거나 k - 최단거리가 홀수면 도착 불가
    if dist > k or (k - dist) % 2 == 1:
        return "impossible"

    answer = dfs(x, y, "", 0)
    return answer if answer else "impossible"

print(solution(3, 4, 2, 3, 3, 1, 5))