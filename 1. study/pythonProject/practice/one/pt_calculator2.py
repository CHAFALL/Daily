'''
(6+5*(2-8)/2)
6528-*2/+
'''

# 일단은 정상적인 수식이 들어오는 것을 전제로...
stack = []
icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}

fx = '(6+5*(2-8)/2)'
susik = ''
for x in fx:
    if x not in '(+-*/)':
        susik += x
    elif x == ')':              # '('까지 pop()
        while stack[-1] != '(': #peek
            susik += stack.pop()
        stack.pop()             # '(' 버림. pop()

    else: # '(+-*/'
        if not stack or isp[stack[-1]] < icp[x] : # 토큰의 우선순위가 더 높으면
            stack.append(x)
        elif isp[stack[-1]] >= icp[x]:
            while stack and isp[stack[-1]] >= icp[x]:
                susik += stack.pop()
            stack.append(x)
print(susik)

for x in susik:
    if x not in '+-/*': # 피연산자면....
        stack.append(int(x))
    else:
        op2 = stack.pop()
        op1 = stack.pop()

        if x == '+':  #(먼저 나온 애가 오른쪽!!)
            stack.append(op1 + op2)
        elif x == '-':
            stack.append(op1 - op2)
        elif x == '/':
            stack.append(op1 // op2)
        elif x == '*':
            stack.append(op1 * op2)

print(stack[0])  # -9