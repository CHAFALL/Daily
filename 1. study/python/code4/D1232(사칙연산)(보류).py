import sys
sys.stdin = open('D1232.txt')


def calc(op, left, right):
    if op == '+':
        result = left + right
    elif op == '-':
        result = left - right
    elif op == '*':
        result = left * right
    elif op == '/':
        result = left / right

    return result


def postorder(v):
    if ch1[v] == 0 and ch2[v] == 0:
        return num[v]
    else:
        left = postorder(ch1[v])
        right = postorder(ch2[v])
        num[v] = calc(op[v], left, right)
        return num[v]


T = 10
for tc in range(1, T + 1):
    N = int(input())
    op = [0] * (N + 1)
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    num = [0] * (N + 1)
    for _ in range(N):
        temp = list(input().split())
        idx = int(temp[0])
        # 연산자 이면 자식 2개 필요
        if temp[1] == '+' or temp[1] == '-' or temp[1] == '*' or temp[1] == '/':
            op[idx] = temp[1]
            ch1[idx] = int(temp[2])
            ch2[idx] = int(temp[3])
        else:  # 피연산자
            num[idx] = int(temp[1])
    ans = postorder(1)
    print(f'#{tc} {int(ans)}')
# -----------------------------------------------------------------------------------
# 동영이 형님꺼
# def postorder(n):
#     if n:
#         a = postorder(tree[n][0])
#         b = postorder(tree[n][1])
#         if tree[n][3] == '+':
#             return a + b
#         elif tree[n][3] == '-':
#             return a - b
#         elif tree[n][3] == '*':
#             return a * b
#         elif tree[n][3] == '/':
#             return a // b
#         else:
#             return tree[n][3]
#
#
# T = 10
# for tc in range(1, T + 1):
#     N = int(input())
#
#     tree = [[0] * 4 for _ in range(N + 1)]
#     for i in range(N):
#         temp = input().split()
#         if len(temp) == 4:
#             tree[int(temp[0])][3] = temp[1]
#             tree[int(temp[0])][0] = int(temp[2])
#             tree[int(temp[0])][1] = int(temp[3])
#             tree[int(temp[2])][2] = int(temp[0])
#             tree[int(temp[3])][2] = int(temp[0])
#         else:
#             tree[int(temp[0])][3] = int(temp[1])
#
#     print(f'#{tc} {postorder(1)}')
