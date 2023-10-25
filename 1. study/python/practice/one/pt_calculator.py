'''
(6+5*(2-8)/2)
6528-*2/+
'''

# 정상적인 수식이 들어오는 것을 전제로...
stack = [0] * 100 # 스택은 돌려가며 씁시다, top만 초기화 하면 되므로
top = -1
icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}

fx = '(6+5*(2-8)/2)'
susik = ''
for x in fx:
    if x not in '(+-*/)':
        susik += x
    elif x == ')': # '('까지 pop()
        while stack[top] != '(': # peek
            susik += stack[top]
            top -= 1
        top -= 1                 # '(' 버림. pop

    else:   # '(+-*/'
        if top == -1 or isp[stack[top]] < icp[x]: # 토큰의 우선순위가 더 높으면
            top += 1    #push
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                susik += stack[top]
                top -= 1
            top += 1    #push
            stack[top] = x

    # 여기부분 더 깔끔하게 만들 수 있을 것임!
print(susik)

# susik = '6528-*2/+'
for x in susik:
    if x not in '+-/*': # 피연산자면....
        top += 1        # push(x)
        stack[top] = int(x)
    else:

        op2 = stack[top]  # pop()
        top -= 1
        op1 = stack[top]  # pop()
        top -= 1
        if x == '+':      # op1 + op2
            top += 1      # push(x)
            stack[top] = op1 + op2
        elif x == '-':
            top += 1      # push(x)
            stack[top] = op1 - op2 # (먼저 나온 애가 오른쪽!!)
        elif x == '/':
            top += 1      # push(x)
            stack[top] = op1 // op2  # (주의!!)
        elif x == '*':
            top += 1      # push(x)
            stack[top] = op1 * op2

print(stack[top]) # -9