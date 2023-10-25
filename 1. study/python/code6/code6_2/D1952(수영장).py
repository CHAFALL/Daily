import sys
sys.stdin = open('D1952.txt')

def dfs(k, cost):
    global min_v
    # 가지치기
    if min_v <= cost:
        return
    if k > 12:
        min_v = cost
        return

    # 가능한 경로로만 루트 짜기
    else:
        # 1일 이용권으로만 한 달 버티기
        dfs(k + 1, cost + day * arr[k])
        # 한달 이용권으로 한 달 버티기
        dfs(k + 1, cost + month)
        # 세달 이용권으로 세 달 버티기
        dfs(k + 3, cost + month3)
        # 1년 이용권으로 1년 버티기
        dfs(k + 12, cost + year)

T = int(input())
for tc in range(1, T + 1):
    day, month, month3, year = map(int, input().split())
    arr = [0] + list(map(int, input().split())) # 주의!!!!!!!!!!
    min_v = 987654321
    dfs(1, 0)
    print(min_v)