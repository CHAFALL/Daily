T = int(input())
for tc in range(1, T+1):
    H , W = map(int, input().split())


    arr = [[0] * W for _ in range(H)]

    i = 1
    for h in range(H): # 행
        for w in range(W): # 열
            arr[h][w +((-2) * w + W-1) * (h % 2)] += i
            i += 1
    
    print(f'#{tc}')
    for q in range(H):
        ans = ' '.join(map(str, arr[q]))
        print(f'{ans}')                