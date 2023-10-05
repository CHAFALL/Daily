import sys
sys.stdin = open('D1234.txt')

# stack으로 풀어보기
# T = 10
# for tc in range(1, T+1):
#     N, number = map(str, input().split()) # 조심
#     N = int(N)
#
#     # 초기설정
#     stack = [0] * 1000
#     top = -1
#
#     for i in range(N):
#         # 비어있는 경우
#         if top == -1:
#             top += 1
#             stack[top] = number[i]
#
#         else:
#             if stack[top] != number[i]:
#                 top += 1
#                 stack[top] = number[i]
#             else:
#                 top -= 1
#
#     print(f'#{tc} ', end='')
#     for i in range(top+1):
#         print(stack[i], end='')
#     print()

#----------------------------------------------------------------
# pop(), append()로 풀기
T = 10
for tc in range(1, T+1):
    N, number = map(str, input().split()) # 조심
    N = int(N)
    # 초기설정
    stack = []
    for i in range(N):
        # 비어있을 때
        if not stack:
            stack.append(number[i])
        else:
            if stack[-1] != number[i]:
                stack.append(number[i])
            else:
                stack.pop()

    print(f'#{tc} ', end='')
    print(''.join(stack))






