import sys
sys.stdin = open('D11871.txt')

# T = int(input())
# for tc in range(1, T+1):
#     text = input()
#     N = len(text)
#     # 초기 설정
#     stack = [0] * 1000
#     top = -1
#
#     for i in range(N):
#         # 비었을 때
#         if top == -1:
#             top += 1
#             stack[top] = text[i]
#         else:
#             if stack[top] != text[i]:
#                 top += 1
#                 stack[top] = text[i]
#             else:
#                 top -= 1
#
#     print(f'#{tc} {top+1}')
#     print(stack) # 덮어쓰기가 아직 안 되어서 남아있는 것을 알 수 있다.

#--------------------------------------------------------------------------
# pop , append 쓰기

# T = int(input())
# for tc in range(1, T+1):
#     text = input()
#     N = len(text)
#     # 초기 설정
#     stack =[]
#     for i in range(N):
#         if not stack:
#             stack.append(text[i])
#
#         else:
#             if stack[-1] != text[i]:
#                 stack.append(text[i])
#             else:
#                 stack.pop()
#
#     print(f'#{tc} {len(stack)}')
#--------------------------------------------------------------------------
# 함수 짜서 풀어보기 (좀 어렵구만)
# def push(stack, item):
#     global top
#     top += 1
#     stack[top] = item
#
# def pop(stack):
#     global top
#     if top == -1:
#         return
#     else:
#         result = stack[top] # pop 리턴 값 있잖아~
#         top -= 1
#         return  result
#
# def is_empty(stack): # 비어있는지 확인 필수!!
#     global top
#     if top == -1:
#         return True
#     else:
#         return False
#
# def peek(stack):
#     return stack[top]
#
# T = int(input())
# for tc in range(1, T+1):
#     text = input()
#     N = len(text)
#     # 초기 설정
#     stack = [0] * 1000
#     top = -1
#
#
#     for i in range(N):
#         if is_empty(stack): # 스택이 비어 있으면 -> push
#             push(stack, text[i])
#         else:               # 스택이 비어 있지 않으면, 파이썬은 잘 못 짜면 맨 끝에것을 가져올지도?(항상 비어있을 때 생각해줘야 됨)
#             # 스택의 맨 위 원소와 비교
#             if peek(stack) == text[i]:
#                 pop(stack)
#             else:
#                 push(stack, text[i])
#
#     print(f'#{tc} {top+1}')
#-------------------------------------------------------------------
# 연습
# T = int(input())
# for tc in range(1, T+1):
#     text = input()
#     N = len(text)
#     # 초기 설정
#     stack = [0] * 1000
#     top = -1
#
#     for i in range(N):
#         # 비었을 때
#         if top == -1:
#             top += 1
#             stack[top] = text[i]
#
#         else:
#             if stack[top] != text[i]:
#                 top += 1
#                 stack[top] = text[i]
#             else:
#                 top -= 1
#
#     print(top+1)
#------------------------------------------------------
# 연습 2
T = int(input())
for tc in range(1, T+1):
    text = input()
    N = len(text)
    # 초기 설정
    stack = []
    for i in range(N):
        if not stack:
            stack.append(text[i])
        else:
            if stack[-1] != text[i]:
                stack.append(text[i])
            else:
                stack.pop()
    print(len(stack))
