import sys
sys.stdin = open('D1222.txt')
def solve(fx):
    stack = []
    susik = ''
    for x in fx:
        # 피연산자면 토큰 출력
        if x != '+':
            susik += x
        # '+' 만나면(stack 비었을 땐 push)
        else:
            if not stack:
                stack.append(x)
            else:
                while stack:
                    susik += stack.pop()
                stack.append(x) # 이거만 실수함
    # 스택에 남아 있는 연산자를 모두 pop하여 출력
    while stack:
        susik += stack.pop()

    for x in susik:
        # 피연산자면 push
        if x != '+':
            stack.append(int(x))
        #  연산자를 만나면 pop해주고 연산 뒤에 다시 push해줌
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(op1+op2)
    # 수식이 끝나면 마지막으로 스택을 pop하여 출력
    return stack.pop()


T = 10
for tc in range(1, T+1):
    N = int(input())
    fx = input()
    print(solve(fx))