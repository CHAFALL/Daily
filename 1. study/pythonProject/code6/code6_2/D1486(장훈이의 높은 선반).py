import sys
sys.stdin = open('D1486.txt')

# 부분집합 문제

def powerset(k, s):
    global min_v

    # 가지치기
    if min_v == 0:
        return
    # 선반 이용 가능해졌을 때
    if B <= s:
        min_v = min(min_v, abs(B - s))
        return

    if k == N:
        return

    else:
        powerset(k + 1, s + arr[k])
        powerset(k + 1, s)


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    min_v = 987654321
    powerset(0, 0)
    print(f'#{tc} {min_v}')
