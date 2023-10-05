T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0
    max_v = 0
    for i in range(len(arr)):
        for j in range(i+1, N):                #값 비교 넣어주기
            if arr[i] <= arr[j]:
                count+=1
            temp = N - arr[i] -i -1 -count
            if temp > max_v:
                max_v = temp
    print(f'#{tc} {max_v}')
