import sys
sys.stdin = open('D1979.txt')

# 0: 벽, 1: 빈칸
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    # 행
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or j == N-1: # 점검 # 여기 elif로 하면 안 됨!!!
                if cnt == K:
                    total += 1
                cnt = 0
    # 열
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or i == N-1: # 점검
                if cnt == K:
                    total += 1
                cnt = 0

    print(f'#{tc} {total}')
