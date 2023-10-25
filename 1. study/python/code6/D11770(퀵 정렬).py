import sys
sys.stdin = open('D11770.txt')


def hoare_partition(a, l, r):
    p = a[l]
    i, j = l, r
    while i <= j:
        # 아래와 같이 = 안 붙이면 arr = [1,1,1,1,0,0,0] 이런거 고장남
        while i <= j and a[i] <= p: # 왼쪽에서 큰 값
            i += 1
        while i <= j and a[j] >= p: # 오른쪽에서 작은 값
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]  # 피봇과 j의 값을 교환

    return j  # 피봇자리

def quick_sort(a, l, r):
    if l < r:
        pivot = hoare_partition(a, l, r)
        quick_sort(a, l, pivot - 1)
        quick_sort(a, pivot + 1, r)
        # 파괴 메소드라서 알아서 고쳐지는 중이구나
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, N-1)
    print(f'#{tc} {arr[N//2]}') # 얘는 파괴 메소드

