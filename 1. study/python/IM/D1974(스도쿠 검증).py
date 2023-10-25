import sys
sys.stdin = open('D1974.txt')

T = int(input())
N = 9
ans = 1


def solve():
    # 행
    for i in range(N):
        C = [0] * (N + 1)
        for j in range(N):
            C[arr[i][j]] += 1
        # 체크
        for o in range(1, N + 1):
            if C[o] != 1:
                return 0

    # 열
    for j in range(N):
        C = [0] * (N + 1)
        for i in range(N):
            C[arr[i][j]] += 1
        # 체크
        for o in range(1, N + 1):
            if C[o] != 1:
                return 0

    # 뭉티
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            C = [0] * (N + 1)
            for p in range(3):
                for q in range(3):
                    C[arr[i + p][j + q]] += 1
            # 체크
            for o in range(1, N + 1):
                if C[o] != 1:
                    return 0

    return 1

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {solve()}')