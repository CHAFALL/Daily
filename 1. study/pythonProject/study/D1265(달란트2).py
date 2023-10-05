import sys
sys.stdin = open('D1265.txt')
T = int(input())
for tc in range(1, T + 1):
    N, P = map(int, input().split())
    # q:몫, r: 나머지
    q = N // P
    r = N % P
    # 일단 나머지 빼고 공평하게 나눠주기
    nums = [q] * P
    # 남은것은 되는대로 1개씩 더 배분해주기
    for i in range(r):
        nums[i] += 1

    # 최대한 공평하게 배분했으니 계산해주기
    temp = nums[0]
    for i in range(1, P):
        temp *= nums[i]

    print(f'#{tc} {temp}')

