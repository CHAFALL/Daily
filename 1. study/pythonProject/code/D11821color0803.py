import sys
sys.stdin = open('D11821')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)] # 이것도 위치 신경 써줘야 되네

    total_counts = 0 # 여기 위치 잘 볼것!!
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                # 보라색이 이미 칠해져 있으면 바로 넘김(카운트 중첩 방지)
                if arr[r][c] == 3:
                    continue
                # 같은 색깔이 아니면 색칠
                if arr[r][c] != color:
                    arr[r][c] += color
                # 보라색이면 카운트 올림
                if arr[r][c] == 3:
                    total_counts += 1

    print(f'#{tc} {total_counts}')




