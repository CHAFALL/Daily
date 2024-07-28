# 몫과 나머지를 활용해야 하나?
# 아니면 그냥 단순 무식하게 DFS? -> 종류가 많아서 pass
# sort 필요할지도? (100종류 이하면)
# 마사카 DP?

def solution(n, money):

    dp = [1] + [0] * n
    for mny in money:
        for price in range(mny, n + 1):
            if price >= mny:
                dp[price] += dp[price - mny]

    return dp[n] % 1_000_000_007


print(solution(5, [1, 2, 5]))