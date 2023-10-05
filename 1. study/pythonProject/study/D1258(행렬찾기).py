import sys
sys.stdin = open('D1258.txt')

# 오른쪽, 아래
di = [0, 1]
dj = [1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = []
    for i in range(N):
        for j in range(N):
            # 용기가 있다면 탐색 시작
            if arr[i][j] != 0:
                for k in range(2):
                    p = 1
                    while True:
                        ni = i + di[k] * p
                        nj = j + dj[k] * p
                        # 아직도 용기가 있다면
                        if 0 <= ni < N and 0 <= nj < N \
                                and arr[ni][nj] != 0:
                            p += 1
                        # 나가거나 빈용기를 만나면
                        else:
                            if k == 0:
                                c = p  # 열의 크기
                            elif k == 1:
                                r = p  # 행의 크기
                            break
                # 영역, 행, 열
                ans.append((r * c, r, c))
                # 탐색했던 것은 치우기
                for x in range(i, i + r):
                    for y in range(j, j + c):
                        arr[x][y] = 0

    ans.sort()

    print(f'#{tc} {len(ans)}', end=' ')
    for i in range(len(ans)):
        print(ans[i][1], ans[i][2], end=' ')
    print()



