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
            arr_total += cnt
            if pre_cnt == arr_cnt:
                pre_cnt = arr_total  # 이제는 우리 깊이야.


            cnt = 0


# 여기에서 찾고자 하는 것이 속한 팀은 현재 차수에서의 총합에서 빼줘야 함!!
# 이거 구현, 변수가 5개???? 이거 맞냐? 배열로 통합할까? 그냥?


# 사촌 관계를 찾는 문제이므로 바로 위 깊이의 배열의 수만 파악하고 있으면
# 되지 않을까?? 그것을 파악하고 있다면 쉽게 될 것 같은데..


# temp에서 찾는 값 바로 이전으로 배열을 짜르고 연속되는 것을 파악하는거지
# 그러면 바로 위 깊이의 배열의 수를 알 수 있을 것이고
