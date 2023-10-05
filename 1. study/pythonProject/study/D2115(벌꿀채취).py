import sys
sys.stdin = open('D2115.txt')

def find():
    max_v = 0
    vi = vj = 0
    for i in range(N):
        for j in range(N - M):
            tmp = 0
            for k in range(j, j + M):
                tmp += arr[i][k]
            if tmp <= C:
                if max_v < tmp:
                    max_v = tmp
                    vi = i
                    vj = j

    return max_v, vi, vj

    # 다 돌았는데 max_v가 0이면? 선택할 수 있는 벌통 중에서 하나 덜 선택하기인데..
    # 이렇게 구현하면 힘들지 않을까?


T = int(input())
for tc in range(1, T + 1):
    # 벌통들의 크기, 선택할 수 있는 벌통의 개수, 꿀을 채취할 수 있는 최대 양
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    print(find())

