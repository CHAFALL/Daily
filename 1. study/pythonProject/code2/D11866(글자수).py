import sys
sys.stdin = open('D11866.txt')
T = int(input())
for tc in range(1,T+1):
    pattern = input()
    text = input()
    M = len(pattern)

    real_total = 0
    for i in range(M):
        counts = 0
        for tx in text:
            if pattern[i] == tx:
                counts +=1

        if real_total < counts:
            real_total = counts

    print(f'#{tc} {real_total}')


