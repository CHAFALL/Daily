import sys
sys.stdin = open('D11767.txt')

def game():
    for i in range(N):
        if i % 2 == 0:
            C1[arr[i]] += 1
        else:
            C2[arr[i]] += 1

        for j in range(10):
            if C1[j] >= 3 or (C1[j] and C1[j + 1] and C1[j + 2]):
                return 1
            if C2[j] >= 3 or (C2[j] and C2[j + 1] and C2[j + 2]):
                return 2

    return 0

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = 12
    C1 = [0] * 12  # 1 # 인덱스 오류를 대비해서 조금 더 키움
    C2 = [0] * 12  # 2

    print(f'#{tc} {game()}')


#-----------------------------------------------------------------------
# 교수님 풀이

