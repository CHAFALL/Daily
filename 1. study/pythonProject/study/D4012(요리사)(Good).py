import sys
sys.stdin = open('D4012.txt')
def comb(k, p, s):
    global min_v
    if k == R:
        # 반대쪽 재료 리스트 구성하기
        other_p = list(set(ALL) - set(p))
        temp1 = temp2 = 0
        # 나 왜 이 아래부분 생각이 안 났냐?
        for i in range(R):
            for j in range(R):
                temp1 += arr[p[i]][p[j]]
                temp2 += arr[other_p[i]][other_p[j]]
        min_v = min(min_v, abs(temp1 - temp2))
        return
    else:
        for i in range(s, N - R + 1 + k):
            comb(k + 1, p + [i], i + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    R = N // 2
    arr = [list(map(int, input().split())) for _ in range(N)]
    ALL = [i for i in range(N)]
    min_v = 99999999999
    comb(0, [], 0)
    print(f'#{tc} {min_v}')