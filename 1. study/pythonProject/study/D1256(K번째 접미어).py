import sys
sys.stdin = open('D1256.txt')

T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    text = input()
    N = len(text)

    # 접미어 리스트 만들어 주기
    arr = []
    for i in range(N):
        arr.append(text[i:])

    # 정렬
    arr.sort()

    # K번째 값 출력
    if K > N:
        print(f'#{tc} none')
    else:
        print(f'#{tc} {arr[K-1]}')

