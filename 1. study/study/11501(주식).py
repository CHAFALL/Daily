'''
3
3
10 7 6
3
3 5 9
5
1 1 3 1 2
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 초기 설정
    money = 0
    max_value = arr[N - 1]
    for i in range(N-1, -1, -1):
        # 만약에 더 많이 올라간 주식이 보인다면? 뒤의 보지도 마!
        if max_value < arr[i]:
            max_value = arr[i]
        else:
            money += max_value - arr[i]

    print(money)

# 더 큰 값을 만났을 때 액션을 취해주면 될 듯.
# 거꾸로???
