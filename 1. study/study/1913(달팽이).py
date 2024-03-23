# di = [-1, 0, 1, 0]  # 상, 우, 하, 좌
# dj = [0, 1, 0, -1]


# N = int(input())  # 홀수만 주어짐
# M = int(input())
#
# # 시작점 정해주기
# start = N // 2

#------------------------------------------------------


di = [1, 0, -1, 0]  # 하, 우, 상, 좌
dj = [0, 1, 0, -1]


N = int(input())  # 홀수만 주어짐
M = int(input())

start = N ** 2  # 시작 수
arr = [[0] * N for _ in range(N)]
i, j, k = 0, 0, 0

while True:
    arr[i][j] = start
    ni = i + di[k]
    nj = j + dj[k]
    # 인덱스 밖으로 나가거나 이미 기입된 값을 만난다면 방향 틀기
    if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] !=0:
        # 방향 틀고 전진도 다시 해줘야 됨
        k = (k + 1) % 4
        ni = i + di[k]
        nj = j + dj[k]
    # 기입될 값 1씩 빼주고 좌표 변경
    start -= 1
    i, j = ni, nj

    # 종료 조건
    if start == 0:
        break

# 배열 출력
for p in range(N):
    print(*arr[p])

# 알고싶은 숫자의 좌표 구하기
for p in range(N):
    for q in range(N):
        if arr[p][q] == M:
            print(p + 1, q + 1)

