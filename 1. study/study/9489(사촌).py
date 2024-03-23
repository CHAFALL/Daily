while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    temp = list(map(int, input().split()))


    pre_cnt = 1
    arr_cnt = 0 # 현재 연속된 배열 덩어리 수
    cnt = 0
    arr_total = 0
    for i in range(2, n): # 첫 놈 빼고, 연속되었는지 check
        if temp[i] == temp[i - 1] + 1:
            cnt += 1
        else:
            arr_cnt += 1
            if pre_cnt == arr_cnt:
                pre_cnt = cnt

            else:
               arr_total += cnt

            cnt = 0







# 트리구조가 부모, 자식들.... 이런구조가 되어야 될 듯.
# 연속된.. 배열 뽑아낼까?? (배열의 수만 알면 되지 않나??)

# 사촌 관계를 찾는 문제이므로 바로 위 깊이의 배열의 수만 파악하고 있으면
# 되지 않을까?? 그것을 파악하고 있다면 쉽게 될 것 같은데..

# 오케이 구상은 끝났고 잘래



# temp에서 찾는 값 바로 이전으로 배열을 짜르고 연속되는 것을 파악하는거지
# 그러면 바로 위 깊이의 배열의 수를 알 수 있을 것이고
