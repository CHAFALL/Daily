def solution(n, money):
    # dp 배열을 초기화하여 0부터 n까지의 금액을 만들 수 있는 방법의 수를 저장
    dp = [0] * (n + 1)
    # dp[0] = 1로 설정하는 이유는, 0원을 만드는 방법은 아무 동전도 사용하지 않는 한 가지 방법뿐이라는 의미입니다.

    dp[0] = 1

    # 각 동전에 대해 반복
    for coin in money:
        # 현재 동전을 사용하여 특정 금액을 만들 수 있는 방법의 수를 업데이트
        for amount in range(coin, n + 1):
            # dp[amount]는 dp[amount - coin] 값을 더하여 업데이트
            dp[amount] += dp[amount - coin]

            # 예를 들어, amount가 5이고 coin이 2라면, dp[5]는 dp[3]의 값을 더함
            # 이는 3원을 만들 수 있는 방법에 2원을 더하여 5원을 만드는 경우를 추가하는 것

    # 최종적으로 dp[n]에는 주어진 금액 n을 만드는 방법의 수가 저장됨
    return dp[n]


# 함수 테스트
print(solution(5, [1, 2, 5]))  # 예상 출력: 4
