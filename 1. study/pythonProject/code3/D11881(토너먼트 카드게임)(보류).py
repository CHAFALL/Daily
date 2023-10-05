import sys
sys.stdin = open('D11881.txt')
def win(r1, r2):
    if arr[r1] == arr[r2]:
        return r1
    else:
        if arr[r1] == 1 and arr[r2] == 2:
                return r2
        elif arr[r1] == 1 and arr[r2] == 3:
                return r1
        elif arr[r1] == 2 and arr[r2] == 1:
                return r1
        elif arr[r1] == 2 and arr[r2] == 3:
                return r2
        elif arr[r1] == 3 and arr[r2] == 1:
                return r2
        elif arr[r1] == 3 and arr[r2] == 2:
                return r1


def game(l, r):
    if l == r: # 재귀호출 종료 조건
        return l # l로 하든 r로 하든 상관 없다.
    else:
        r1 = game(l, (l+r) // 2)
        r2 = game((l + r) // 2 + 1, r)
        # 더 이상 재귀호출 할 것이 없으면 내려감
        return win(r1, r2) # 여기가 이해가 안 감
                           # 반환값
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    print(f'#{tc} {game(0, N-1) + 1}')