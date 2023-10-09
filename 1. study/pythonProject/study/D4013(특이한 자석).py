import sys
sys.stdin = open('D4013.txt')


def dfs(num, dir):  # 자석 번호, 도는 방향
    cnt[num] = 1  # 방문 체크

    if num != 0:  # 젤 왼쪽이 아니면, 왼쪽 체크
        if arr[num][6] != arr[num - 1][2] and not cnt[num - 1]:
            dfs(num - 1, -1 * dir)
    if num != 3:
        if arr[num][2] != arr[num + 1][6] and not cnt[num + 1]:
            dfs(num + 1, -1 * dir)

    # 도는 것 구현
    if dir == -1:  # 반시계 방향
        arr[num][0], arr[num][1], arr[num][2], arr[num][3], \
        arr[num][4], arr[num][5], arr[num][6], arr[num][7] \
            = arr[num][1], arr[num][2], arr[num][3], arr[num][4], \
              arr[num][5], arr[num][6], arr[num][7], arr[num][0]
    elif dir == 1:  # 시계방향
        arr[num][0], arr[num][1], arr[num][2], arr[num][3], \
        arr[num][4], arr[num][5], arr[num][6], arr[num][7] \
            = arr[num][7], arr[num][0], arr[num][1], arr[num][2], \
              arr[num][3], arr[num][4], arr[num][5], arr[num][6]


# 비교 왼쪽: 6, 비교 오른쪽: 2
# 시계 방향: 1, 반시계 방향: -1
# N : 0, S : 1
T = int(input())
for tc in range(1, T + 1):
    K = int(input())  # 회전 횟수
    arr = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K):
        num, dir = map(int, input().split())
        cnt = [0, 0, 0, 0]  # 회전횟수(최대 1번)
        dfs(num - 1, dir)

    ans = 0
    for i in range(4):
        if arr[i][0] == 1:
            ans += 2 ** i

    print(f'#{tc} {ans}')
