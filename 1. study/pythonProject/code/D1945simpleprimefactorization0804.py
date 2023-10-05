import sys
sys.stdin = open('D1945')

T = int(input())
num_list = [2, 3, 5, 7, 11]
for tc in range(1, T+1):
    number = int(input())

    k = 0
    C = [0] * 5

    while k < 5:
        if number % num_list[k] == 0:
            number = number // num_list[k]
            C[k] += 1
        else:
            k+=1

    print(f'#{tc}', end = ' ')
    print(*C)


