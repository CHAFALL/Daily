import sys
sys.stdin = open('D11753.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    i = 1
    ans = ''
    while i < 13 and N:
        if N - 2**-i >= 0:
            N -= 2**-i
            ans += '1'
        else:
            ans += '0'
        i += 1


    if N != 0:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {ans}')
#-------------------------------------------------------------
def solve(n):
    rst = ''
    counts = 0
    while counts < 13 and n:
        n *= 2
        counts += 1
        # 2를 곱한 값이 1이상일 때
        if n >= 1:
            rst += '1'
            n -= 1  # 소수점 아래만 필요
        else:
            rst += '0'
    if counts >= 13:
        return 'overflow'
    else:
        return rst

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    print(f'#{tc} {solve(N)}')







