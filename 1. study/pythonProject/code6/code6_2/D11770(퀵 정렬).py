import sys
sys.stdin = open('D11770.txt')

def hoare_partition(a, l, r):
    p = a[l] # 피봇 지정(그냥 맨 앞으로 함)
    i, j = l, r
    while i <= j:
        while i <= j and a[i] <= p: # 왼쪽에서 큰 값 찾기
            i += 1
        while i <= j and a[j] >= p: # 오른쪽에서 작은 값 찾기
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
    else:
        a[l], a[j] = a[j], a[l] # 피봇 위치와 j를 교환

    return j # 피봇 자리

# 정확한 피봇 위치를 찾아서 연산량을 줄임
def quick_sort(a, l, r):
    if l < r:
        pivot = hoare_partition(a, l, r)
        quick_sort(a, l, pivot - 1)
        quick_sort(a, pivot + 1, r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, N - 1) # 얘는 파괴 메소드
    print(f'#{tc} {arr[N // 2]}')