import sys
sys.stdin = open('D1224.txt')
def solve(fx):
    stack = []
    susik = ''
    for x in fx:
        if x not in '(+*)':
            susik += x
        elif x in ')':
            while stack[-1] != '(':
                susik += stack.pop()
            stack.pop() # 왼쪽 괄호 버림
        else: #'(+*' # 여기 부분 주의 깊게 보기!!
            while stack and icp[x] <= isp[stack[-1]]:
                susik += stack.pop()
            stack.append(x)
    while stack:
        susik += stack.pop()

    for x in susik:
        if x not in '+*':
            stack.append(int(x))
        else:
            op2 = stack.pop()
            op1 = stack.pop()

            if x == '+':  # (먼저 나온 애가 오른쪽!!)
                stack.append(op1 + op2)
            elif x == '*':
                stack.append(op1 * op2)

    return stack.pop()

icp = {'(': 3, '*': 2, '+': 1}  # 스택 밖
isp = {'(': 0, '*': 2, '+': 1}  # 스택 안
T = 10
for tc in range(1, T+1):
    N = int(input())
    fx = input()
    print(solve(fx))
