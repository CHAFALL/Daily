# ws_5_3.py

# 아래 함수를 수정하시오.
def sort_tuple(tup):        #sorted 함수로 풀기
    sort_tup = tuple(sorted(tup))

    return sort_tup

result = sort_tuple((5, 2, 8, 1, 3))
print(result)
#````````````````````````````````````````````````
# 이것도 불변이라 sort() 없겠지?, 리스트 변환 ㄱ
# def sort_tuple(tup):
#     tup_list = list(tup)
#     tup_list.sort()
#     sort_tup = tuple(tup_list)

#     return sort_tup      

# result = sort_tuple((5, 2, 8, 1, 3))
# print(result)
#``````````````````````````````````````````````````
# sort함수 만드는 법 연습 겸 한번 만들어 볼까? (미완.. 어렵네..)

# def sort_tuple(tup):
#     tup_list = list(tup)
#     temp = tup_list[0]
#     for tp in tup_list:
#         if tp < temp:
#             tp, temp = temp, tp


#     return       

# result = sort_tuple((5, 2, 8, 1, 3))
# print(result)