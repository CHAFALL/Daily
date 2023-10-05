import sys
sys.stdin = open('D1865.txt')

# 순열을 이용하는 문제
def perm(k, s): # 깊이, 현재 합
    global max_v
    # 가지치기
    if max_v >= s:
        return
    if k == N:
        # 하고 싶은 일 하기
        max_v = s
        return
    else:
        for i in range(N):
            if visited[i] == 0:
                visited[i] = 1
                perm(k + 1, s * arr[k][i] * 0.01)
                visited[i] = 0



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_v = 0

    perm(0, 1)
    print(f'#{tc} {max_v * 100:.6f}')
