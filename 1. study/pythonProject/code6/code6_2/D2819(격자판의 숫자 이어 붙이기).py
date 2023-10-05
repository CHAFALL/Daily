import sys
sys.stdin = open('D2819.txt')

def dfs(k, i, j, nums):
    if k == 7:
        result.add(nums)
        return
    else:
        for p in range(4):
            ni = i + di[p]
            nj = j + dj[p]
            if 0 <= ni < N and 0 <= nj < N:
                dfs(k + 1, ni, nj, nums + arr[ni][nj])


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
N = 4
for tc in range(1, T + 1):
    # 문자열로 받으면 편할 것이다.
    arr = [input().split() for _ in range(N)]
    # 중복 제거는 set
    result = set()
    for i in range(N):
        for j in range(N):
            # 하나 넣고 시작
            dfs(1, i, j, arr[i][j])

    print(f'#{tc} {len(result)}')