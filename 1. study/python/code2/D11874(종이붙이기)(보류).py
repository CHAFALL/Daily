import sys; sys.stdin = open('D11874.txt')

# 재귀를 사용한 풀이
def f(n):
    if n <= 1:
        return 1
    else:
        return f(n - 1) + 2 * f(n - 2)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    print(f'#{test_case} {f(N // 10)}')

# dp를 이용한 풀이
# memo = [1, 1]
# for i in range(2, 31):
#     memo.append(memo[i-1] + 2*memo[i-2])

# T = int(input())
# for test_case in range(1, T + 1):
#    N = int(input())
#    print(f'#{test_case} {f(N//10)}')