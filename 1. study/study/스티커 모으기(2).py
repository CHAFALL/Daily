def solution(sticker):
    answer = 0

    N = len(sticker)
    if N == 1:
        return sticker[0]

    dp = [[0] * N for _ in range(2)]

    dp[0][0] = sticker[0]  # 1번째 사용
    dp[0][1] = sticker[0]

    dp[1][1] = sticker[1]  # 1번째 사용 x

    # 1번째 사용 case
    for i in range(2, N - 1):
        dp[0][i] = max(dp[0][i - 2] + sticker[i], dp[0][i - 1])

    # 1번째 사용 x case
    for i in range(2, N):
        dp[1][i] = max(dp[1][i - 2] + sticker[i], dp[1][i - 1])

    answer = max(dp[0][N - 2], dp[1][N - 1])

    return answer
print(solution([14, 6, 5, 11, 3, 9, 2, 10]))