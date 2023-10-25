import sys
sys.stdin = open('D11773.txt')

# 중복이 없으니 트리 형식이 좋다.
def bt(k, cnt, battery): # 교환횟수, 배터리 양
    global min_v
    # 가지치기
    if cnt >= min_v:
        return

    if k == N - 1:
        min_v = cnt
        return

    # 가능성 있는 것만
    else:
        # 배터리가 있을 때만 그냥 지나칠 수 있다!!
        if battery:
            bt(k + 1, cnt, battery - 1)
        bt(k + 1, cnt + 1, arr[k] - 1)


T = int(input())
for tc in range(1, T + 1):
    N, *arr = map(int, input().split())
    min_v = 987654321
    # 출발지의 교환은 교환횟수에 영향 x
    bt(1, 0, arr[0] - 1)

    print(f'#{tc} {min_v}')