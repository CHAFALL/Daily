import sys
sys.stdin = open('D11869.txt')

T = int(input())
for tc in range(1, T+1):
    pattern = input()
    text = input()

    if text.find(pattern) == -1:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')
