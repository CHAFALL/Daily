import sys
sys.stdin = open('D11884.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Q = input().split()

    for _ in range(M):
        Q.append(Q.pop(0))

    print(Q[0])

