arr = list(input())
N = len(arr)

stack = []
bracket = []

# 괄호 쌍 찾기
for i in range(N):
    if arr[i] == '(':
        stack.append(i)
    elif arr[i] == ')':
        s = stack.pop()
        bracket.append((s,i))

M = len(bracket)



print(bracket)