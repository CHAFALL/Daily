import sys
sys.stdin = open('D11885.txt')

T = int(input())
for tc in range(1, T+1):
    # 화덕, 치즈의 양
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    Q = []
    # 넣고 시작
    for i in range(1, N + 1): # 인덱스로 접근 할 것임
        Q.append(i)

    idx = N + 1
    while len(Q) > 1:
        pizza = Q.pop(0) # 0번 화로에 있는 피자는?
        cheese[pizza] //= 2 # 그 피자의 치즈 반으로 줄이기
        # 치즈가 다 녹았을 때
        if cheese[pizza] == 0:
            # 넣을 피자가 남았니?
            if idx <= M:
                Q.append(idx)
                idx += 1
        # 피자가 덜 녹았으면 다시 넣음
        else:
            Q.append(pizza)

    print(Q[0])


#-----------------------------------------------------------
# 나 뭐 틀림?
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     cheese = [0] + list(map(int, input().split()))
#
#     Q = []
#     for i in range(1, N + 1):
#         Q.append(i)  # 피자 번호가 원소로 들어감
#     idx = N + 1  # 다음에 들어갈 피자 번호
#
#     while len(Q) > 1:
#         pizza = Q.pop(0)
#         cheese[pizza] //= 2
#
#         if cheese[pizza] > 0:
#             Q.append(pizza)
#         elif idx <= M:
#             Q.append(idx)
#             idx += 1
#
#     print(f"#{tc} {Q[0]}")

