import sys
sys.stdin = open('D2819.txt')
# 격자칸을 다시 가도 된다-> visited를 안 써도 된다.

# 대신 이거는 예전에 썻던거네는 알아야 됨(내가 처음에 생각한 것과 다른 느낌인 듯)
# 나는 격자 숫자 하나로 생각했다면, 강사는 7자리 수를 예전에 썻던 것인지...

# 격자 숫자 하나까지 구별해야 한다면 우예 해야 될까?

# 그래서 반드시 완전탐색을 해야한다.(가지치기 불가)
# 마지막까지 봐야지만 동일한 숫자라는 것이 판단이 되므로

# 문자열로 하면 편함
# 격자판(4 * 4) * 7자리 => 완탐 가능하겠네
# 중복을 제거할 방법(set)

#-------------------------------------------------------------
# 1. 재귀 돌리면서 숫자를 붙인다
# 2. 숫자가 7자리가 되면
# 3. set에다 넣는다

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 특정 위치를 기점으로 상하좌우 문자를 붙여야 하므로
# 파라미터로 좌표값도 받아야 한다.
def dfs(y, x, number):

    # 길이가 7이 되면 재귀 종료
    if len(number) == 7:
        result.add(number)
        return

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        # 갈 수 없는 위치면 continue
        if ny < 0 or ny >= 4:
            continue
        if nx < 0 or nx >= 4:
            continue

        # 갈 수 있다면, 다음 위치로 이동
        dfs(ny, nx, number + maps[ny][nx])


T = int(input())
for tc in range(1, T + 1):
    # 서로 다른 수를 합친다=> 문자열이 더 좋다.
    maps = [input().split() for _ in range(4)]
    # 7자리 수를 중복 제거하여 저장
    result = set()
    # 시작지점을 모두 보아야 한다.
    for i in range(4):
        for j in range(4):
            dfs(i, j, maps[i][j])

    print(f'#{tc} {len(result)}')