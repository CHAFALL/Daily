N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0])) # 종료 시간을 기준으로 정렬
finish = ans = 0
for i in range(N):
    if finish <= arr[i][0]: # 만약에 종료시간보다 시작시간이 크다면
        ans += 1
        finish = arr[i][1] # 종료 시간 갱신

print(ans)
