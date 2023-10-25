import sys
sys.stdin = open('D1952.txt')

def dfs(k, cost):
    global ans

    if cost > ans:
        return

    # 기저 조건
    if k > 12:
        ans = min(ans, cost)
        return

    # 1일 이용권으로 모두 구입
    dfs(k + 1, cost + day * plan[k])
    # 한달 이용권 구입
    dfs(k + 1, cost + month)
    # 세달 이용권 구입
    dfs(k + 3, cost + month3)
    # 1년 이용권 구입
    dfs(k + 12, cost + year)

T = int(input())
for tc in range(1, T + 1):
    day, month, month3, year = map(int, input().split())
    plan = [0] + list(map(int, input().split()))

    ans =987654321

    dfs(1, 0)
    print(f'#{tc} {ans}')