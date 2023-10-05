import sys
sys.stdin = open('D3499.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = input().split()
    # 반으로 자르기
    half = N // 2 + N % 2 # 홀수면 하나 더
    front = []
    back = []
    for i in range(half):
        front.append(arr[i])
    for i in range(half, N):
        back.append(arr[i])
    # 합치기
    full = []
    for i in range(N//2):
        full.append(front[i])
        full.append(back[i])

    # 홀수면 앞에 하나 더 있으니
    if N % 2 == 1:
        full.append(front[-1])

    print(f'#{tc}',*full)


