import sys
sys.stdin = open('D11775.txt')

# 순열을 이용하는 문제

def perm(k, s):  # 깊이, 현재 합
    global min_v

    # 가지치기
    if s >= min_v:
        return
    if k == N:
        # 하고 싶은 일 하기
        min_v = min(min_v, s)
        return

    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                perm(k + 1, s + arr[k][i])
                visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    # 인덱스 접근 할 것이라 임시 배열 필요 없음
    min_v = 987654321
    perm(0, 0)

    print(f'#{tc} {min_v}')
