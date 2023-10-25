import sys
sys.stdin = open('D1989.txt')

T = int(input())
for tc in range(1, T+1):
    text = input()
    N = len(text)

    flag = 1
    for i in range(N // 2):
        if text[i] != text[N-1-i]:
            flag = 0
            break

    print(f'#{tc} {flag}')
