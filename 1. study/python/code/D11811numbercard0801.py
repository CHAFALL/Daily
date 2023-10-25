import sys
sys.stdin = open('D11811')

T= int(input())
K = 9
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    C = [0] * (K+1)

    # 카운팅
    for i in range(N):
        C[arr[i]] += 1

    max_idx = 0
    for i in range(K+1): # 여기 범위 할당 조심하기(카운트 기준으로 해야함)
        if C[max_idx] <= C[i]:
            max_idx = i

    print(max_idx, C[max_idx])
