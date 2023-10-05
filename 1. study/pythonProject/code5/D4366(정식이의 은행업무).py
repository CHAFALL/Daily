import sys
sys.stdin = open('D4366.txt')

# T = int(input())
# for tc in range(1, T + 1):
#     binary = list(map(int, input()))
#     trinary = list(map(int, input()))
#
#     N2 = len(binary)
#     N3 = len(trinary)
#
#     # 이진수 값 하나만 변화되는 것 받기
#     bi_list = []
#     for i in range(N2):
#         tmp_binary = binary[:]
#         tmp_binary[i] = ((tmp_binary[i]) + 1) % 2
#         bi_list.append(tmp_binary)
#
#     # 삼진수 값 하나만 변화되는 것 받기
#     tri_list = []
#     for i in range(N3):
#         for j in range(1, 3):
#             tmp_trinary = trinary[:]
#             tmp_trinary[i] = ((tmp_trinary[i]) + j) % 3
#             tri_list.append(tmp_trinary)
#
#     # 이진수 먼저 십진수로 바꾸기
#     b_list = []
#     for i in range(N2):
#         b = 0
#         for j in range(N2):
#             b += bi_list[i][j] * (2 ** (N2 - 1 -j))
#         b_list.append(b)
#
#     # 삼진수 십진수로 바꾸면서 이진수의 십집수랑 같은 거 있으면 바로 나오기
#     for i in range(N3 * 2):
#         t = 0
#         for j in range(N3):
#             t += tri_list[i][j] * (3 ** (N3 - 1 - j))
#
#         if t in b_list:
#             print(f'#{tc} {t}')
#             break

#--------------------------------------------------------------------------
# 이진수나 3진수를 10진수로 변환 할 때
# a = a * 2 + bi_list[i][j] 요런 느낌으로.
# 교수님 방식

T = int(input())
for tc in range(1, T + 1):
    A = input()  # 2진수
    B = list(map(int, input()))  # 3진수

    N = len(A)  # N 자릿수 2진수
    M = len(B)  # M 자릿수 3진수

    binary = int(A, 2)  # 정수로 변환
    bin_list = [0] * N  # 각 비트를 반전시킨 수 N개 저장
    for i in range(N):  # 각 비트를 반전시킨 2진수 만들기
        bin_list[i] = binary ^ (1 << i)

    for i in range(M):  # 3진수의 B[i]자리를 바꾼 숫자 만들기
        num1 = 0  # (B[i] + 1) % 3
        num2 = 0  # (B[i] + 2) % 3
        for j in range(M):
            if i != j:
                num1 = num1 * 3 + B[j]
                num2 = num2 * 3 + B[j]

            else:
                num1 = num1 * 3 + (B[j] + 1) % 3
                num2 = num2 * 3 + (B[j] + 2) % 3


        if num1 in bin_list:
            ans = num1
            break  # for i

        if num2 in bin_list:
            ans = num2
            break  # for i

    print(f'#{tc} {ans}')

