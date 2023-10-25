import sys
sys.stdin = open('D2007.txt')

T = int(input())
for tc in range(1, T+1):
    text = input()
    N = len(text)
    i = 1
    while True:
        if text[0 : i] == text[i : 2 * i]:
            print(f'#{tc} {i}')
            break
        i += 1