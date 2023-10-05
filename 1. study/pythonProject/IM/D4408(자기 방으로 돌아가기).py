import sys
sys.stdin = open('D4408.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 201
    for i in range(N):
        a, b = map(int, input().split())
        # 복도 번호로 바꾸기
        a = (a + a % 2) // 2
        b = (b + b % 2) // 2
        for j in range(min(a, b), max(a, b)+1):
            cnt[j] += 1

    print(f'#{tc} {max(cnt)}')