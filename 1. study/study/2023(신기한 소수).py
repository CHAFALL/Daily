import math

# 개선(약수의 성질을 이용)
# 모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이룸을 이용
# 따라서 우리는 특정한 자연수의 모든 약수를 찾을 때 가운데 약수(제곱근)까지만 확인하면 됨
# ex) 16이 2로 나누어떨어진다는 것은 8로도 나누어떨어진다는 것을 의미

def is_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어 떨어진다면 소수 x
        if x % i == 0:
            return False
    # 나누어 떨어지는 것이 없다면 소수
    return True

# 기본
# def is_prime_number(x):
#     # 2부터 (x-1)까지의 모든 수를 확인하여
#     for i in range(2, x):
#         # x가 해당 수로 나누어 떨어진다면 소수 x
#         if x % i == 0:
#             return False
#     # 나누어 떨어지는 것이 없다면 소수
#     return True

def back(num, v): # 숫자, 깊이
    # 종료 조건
    if v == N:
        print(num)
        return
    for i in range(1, 10):
        if is_prime_number(num * 10 + i):
            back(num * 10 + i, v + 1)


N = int(input())

back(2, 1)
back(3, 1)
back(5, 1)
back(7, 1)