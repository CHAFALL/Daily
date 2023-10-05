import sys
sys.stdin = open('D1225.txt')

T = 10
for _ in range(1, T+1):
    tc = int(input())
    Q = list(map(int, input().split()))

    i = 0
    while True:
        temp = Q.pop(0)
        temp -= i % 5 + 1

        if temp < 0:
            temp = 0
        Q.append(temp)

        if temp == 0:
            print(*Q)
            break

        i += 1



