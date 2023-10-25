import sys
sys.stdin = open('D11825')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(10):
        temp_idx = i

        if i % 2 == 0: # 홀짝 조건을 for j 보다 밖에 해줘야하네 아.. 맞네~
            for j in range(i + 1, N):
                if arr[temp_idx] < arr[j]:
                    temp_idx = j
        else:
            for j in range(i + 1, N):
                if arr[temp_idx] > arr[j]:
                 temp_idx = j

        arr[temp_idx], arr[i] =arr[i], arr[temp_idx]

    print(f'#{tc}', end=' ')
    for i in range(10):
        print(arr[i], end=' ')
    print()



