T = int(input())
for tc in range(1, T+1):
    N = int(input())


    arr = [[0] * N for _ in range(N)]

    i = 1
    for h in range(N): # 행
        arr[h][0] += i
        i += 1
    
    for h in range(N): # 행
        for w in range(1, N): # 열
            arr[h][w] += (arr[h][0]) * (w+1)
            
    print(f'#{tc}')
    for q in range(N):
        ans = ' '.join(map(str, arr[q]))
        print(f'{ans}')                