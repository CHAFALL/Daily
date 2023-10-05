import sys
sys.stdin = open('D11870.txt')

# def solve(text):
#     # 초기 설정
#     stack = []
#
#     for i in range(N):
#         # 비어있을 때
#         if not stack:
#             if text[i] == '(' or text[i] == '{':
#                 stack.append(text[i])
#             elif text[i] == ')' or text[i] == '}':
#                 return 0
#
#         # 비어 있지 않을 때도 append 해줘야지!!! ㅄ아
#         else:
#             if text[i] == '{' or text[i] == '(':
#                 stack.append(text[i])
#             # 짝 비교
#             elif text[i] == '}' or text[i] == ')':
#                 temp = stack.pop() # 먼저 꺼내고 비교
#                 if temp == '{' and text[i] != '}':
#                     return 0
#                 elif temp == '(' and text[i] != ')':
#                     return 0
#
#     if stack: # 왼쪽괄호가 더 많을 때
#         return 0
#
#     return 1
#
# T = int(input())
# for tc in range(1, T+1):
#     text = input()
#     N = len(text)
#
#     print(f'#{tc} {solve(text)}')


# 오류 발생할 때
#1. 스택이 비어있는 데 오른쪽 괄호 들어오는 경우 (오른쪽 괄호가 더 많거나 먼저 나옴)
#2. pop으로 꺼낸 값이랑 이번에 들어오고 있는 괄호랑 짝이 안 맞을 때
#3. 괄호가 남아있는 경우 (왼쪽 괄호가 더 많음)
#-----------------------------------------------------------------------------
# 교수님 방식 (받는 것을 먼저 생각?)
# def solve(str):
#     stack = []
#
#     # 문자열을 스캔
#     for i in range(len(str)):
#         if str[i] == '(' or str[i] == '{':  # 왼쪽 괄호 일 때
#             stack.append(str[i])
#         elif str[i] in [')', '}']:  # 오른쪽 괄호 일 때
#             if not stack:  # is_empty : len(stack) == 0
#                 return 0
#             else:
#                 temp = stack.pop()
#
#                 # 같은종류인지 검사
#                 if str[i] == ')' and temp != '(':
#                     return 0
#                 elif str[i] == '}' and temp != '{':
#                     return 0
#
#     if stack: return 0  # 왼쪽남을때  len(stack) != 0
#
#     return 1  # 앞에서 다 통과하면 1을 리턴
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     str = input()
#     print(f'#{tc} {solve(str)}')

#--------------------------------------------------------------
# 연습
T = int(input())
for tc in range(1, T+1):
    text = input()
    stack = []
    N = len(text)

    result = 1
    for i in range(N):
        # 비어있을 때
        if not stack:
            if text[i] == '{' or text[i] == '(':
                stack.append(text[i])
            elif text[i] == '}' or text[i] == ')':
                result = 0

        else:
            if text[i] == '{' or text[i] == '(':
                stack.append(text[i])
            # 먼저 꺼내고 확인해야한다는 것 기억!!!!!
            elif text[i] == '}' or text[i] == ')':
                temp = stack.pop()

                if temp == '{' and text[i] != '}':
                    result = 0

                elif temp == '(' and text[i] != ')':
                    result = 0
    if stack:
        result = 0

    print(result)



