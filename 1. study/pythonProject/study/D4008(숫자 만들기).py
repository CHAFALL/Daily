import sys
sys.stdin = open('D4008.txt')

def dfs(k, plus, minus, mul, div, s):
    global min_v, max_v

    if k == N:
        min_v = min(min_v, s)
        max_v = max(max_v, s)
        return
    else:
        if plus:
            dfs(k + 1, plus - 1, minus, mul, div, s + nums[k])
        if minus:
            dfs(k + 1, plus, minus - 1, mul, div, s - nums[k])
        if mul:
            dfs(k + 1, plus, minus, mul - 1, div, s * nums[k])
        if div:
            dfs(k + 1, plus, minus, mul, div - 1, int(s / nums[k]))



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    op = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    min_v = 9999999999
    max_v = -9999999999
    dfs(1, op[0], op[1], op[2], op[3], nums[0])

    print(f'#{tc} {max_v - min_v}')
#====================================================
def perm(N, k, op):
    global min_v, max_v
    if N == k:
        # 여기 부분 수정
        temp = arr[0]
        # 연산자에 맞게 두 수 연산해주기
        for i in range(N):
            if op[i] == '+':
                temp += arr[i + 1]
            elif op[i] == '-':
                temp -= arr[i + 1]
            elif op[i] == '*':
                temp *= arr[i + 1]
            elif op[i] == '/':
                if temp < 0:  # 음수 일때 나누는 조건 고려
                    temp = -((-temp) // arr[i + 1])
                else:
                    temp //= arr[i + 1]
        if min_v > temp:
            min_v = temp
        if max_v < temp:
            max_v = temp
        return
    else:
        for i in range(k, N):
            op[k], op[i] = op[i], op[k]
            perm(N, k + 1, op)
            op[k], op[i] = op[i], op[k]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = N - 1
    op_arr = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    op_list = ['+', '-', '*', '/']
    op = []
    min_v = 9999999999
    max_v = -9999999999
    # 연산자 리스트 만들어주기(이것을 순열할 것)
    for i in range(4):
        for j in range(op_arr[i]):
            op.append(op_list[i])

    perm(M, 0, op)
    print(f'#{tc} {max_v - min_v}')
