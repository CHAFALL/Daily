import sys
sys.stdin = open('D1258.txt')
# 아래쪽, 오른쪽
di = [1, 0]
dj = [0, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    check = []
    for i in range(N):
        for j in range(N):
            # 0이 아니면 탐색 시작
            if arr[i][j] != 0:
                area = 1
                for k in range(2):
                    p = 1
                    while True:
                        ni = i + di[k] * p
                        nj = j + dj[k] * p
                        # 빈 용기가 아니면
                        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 0:
                            p += 1
                        # 나가거나 빈 용기이면
                        else:
                            # 행과 열 헷갈리기 쉬움... 조심
                            # 행
                            if k == 0:
                                r = p
                            # 열
                            elif k == 1:
                                c = p
                            # 넓이
                            area *= p
                            break
                check.append((area, r, c))
                # 부시기
                for x in range(i, i + r):
                    for y in range(j, j + c):
                        arr[x][y] = 0

    check.sort()

    print(f'#{tc} {len(check)}', end= ' ')
    for i in range(len(check)):
        print(check[i][1], check[i][2], end= ' ')
    print()



