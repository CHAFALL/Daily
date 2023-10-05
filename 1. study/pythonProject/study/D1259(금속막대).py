import sys
sys.stdin = open('D1259.txt')

# 조건에 빠졌지만 나사가 남는 것은 없다고 합니다.(모든 것이 다 꽂힘)

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    temp = list(map(int, input().split()))

    # 수나사 암나사 묶어주기
    arr = []
    for i in range(n):
        male, female = temp[2 * i], temp[2 * i + 1]
        arr.append((male, female))

    # 암나사 순으로 정렬(뭔가 이렇게 하면 덜 돌것 같음)
    # 둘 다 해본 결과 별 차이가 없었다고 한다..
    # arr.sort(key=lambda x : x[1])

    ans = [arr.pop(0)] # 첫 블록으로 아무것이나 정함(어차피 꽂다보면 정렬됨)
    i = 0
    j = 0 # 꽂은 블록 길이를 알기 위해
    while arr:
        # 앞에 꽂을 수 있다면 꺼내서 꽂고 다시 처음 블록부터 찾기
        if arr[i][1] == ans[0][0]:
            ans.insert(0, arr.pop(i))
            i = 0
            j += 1
        # 뒤에 꽂을 수 있다면
        elif arr[i][0] == ans[j][1]:
            ans.append(arr.pop(i))
            i = 0
            j += 1
        else:
            i += 1

    print(f'#{tc}', end=' ')
    for i in range(len(ans)):
        print(*ans[i], end=' ')
    print()