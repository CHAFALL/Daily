# 행과 열이 반대로 되어있는 문제

def solution(m, n, puddles):
    answer = 0

    # 행과 열 원래 방식으로 바꿔주기
    puddles = [[b, a] for [a, b] in puddles]

    # 1부터 시작하므로.. (dp 초기화)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [i, j] in puddles:  # 웅덩이 위치면 값 계산에 영향 안 미치게 0으로
                dp[i][j] = 0
            else:  # 현재 칸은 왼쪽 칸, 위 칸의 합산이다.
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1])

    return dp[i][j] % 1000000007

print(solution(4, 3, [[2,2]]))