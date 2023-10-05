import sys
sys.stdin = open('D5658.txt')
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    M = N // 4
    check = set() # 중복 방지
    nums = list(input())

    # 모든 경우를 생성할려면 M번 필요
    for _ in range(M):
        # 4등분하기
        for i in range(4):
            s, e = i * M, (i+1) * M
            tmp = nums[s:e]
            tmp = int(''.join(tmp), 16) # 16진수 10진수로 바꾸기
            check.add(tmp) # 중복체크
        nums.append(nums.pop(0)) # 맨 앞의 수 맨 뒤로 보내기
    # sort를 위해 리스트로 변환 후 k번째 값 구하기
    check = list(check)
    check.sort(reverse=True)
    print(f'#{tc} {check[K-1]}')


