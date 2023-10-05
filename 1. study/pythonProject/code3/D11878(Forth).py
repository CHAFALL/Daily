import sys
sys.stdin = open('D11878.txt')

def solve(susik):
    stack = []
    for x in susik:
        # 피연산자이면 push
        if x not in '+-*/.':
            stack.append(int(x))
        # 연산자를 만나면 pop해주고 연산 뒤에 다시 push해줌
        elif x in '+-*/':
            if len(stack) < 2:
                return 'error'
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if x == '+':
                    stack.append(op1 + op2)
                if x == '-':
                    stack.append(op1 - op2)
                if x == '*':
                    stack.append(op1 * op2)
                if x == '/':
                    stack.append(op1 // op2)

        # 수식이 끝나면 마지막으로 스택을 pop하여 출력
        else:  # '.'
            if len(stack) > 1:
                return 'error'

    return stack.pop()

T = int(input())
for tc in range(1, T+1):
    susik = input().split()

    print(solve(susik))


