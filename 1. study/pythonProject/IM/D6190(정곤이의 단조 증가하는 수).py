import sys
sys.stdin = open('D6190.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    danjo = []
    for i in range(N-1):
        for j in range(i+1, N):
            temp = arr[i] * arr[j]
            if temp > 10: # 두 자리 수 이상
                temp = str(temp) # 각 자리 분리하기 위해
                for t in range(len(temp)-1):
                    if temp[t] > temp[t+1]:
                        break
                else:
                    danjo.append(int(temp))
    if danjo:
        print(f'#{tc} {max(danjo)}')
    else:
        print(f'#{tc} -1')



