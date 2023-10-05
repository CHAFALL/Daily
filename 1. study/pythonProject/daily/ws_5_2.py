# def remove_duplicates(lst):
#     new_list = list(set(lst))
    
#     return new_list


# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(result)

#----------------------------------------------------

def remove_duplicates(lst): #좋네 방법
    new_list = []
    for l in lst:
        if l not in new_list:
            new_list.append(l)

    return new_list


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)

#``````````````````````````````````````````````````````````


# def remove_duplicates(lst): #카운팅 배열을 만들어서 풀기  #이건 난도가 좀 있어서 일단 참고만(나중에 최빈수 구할 때 이용됨)
#     counts = [0] * (5+1) # 인덱스 계산 편하게 할려고 1더함

#     for l in lst:
#         counts[l] +=1 #리스트의 인덱스 값을 기준으로 값 증가
    
#     # count에서 값이 0아닌 인덱스만 lst에 추가
#     lst = []
#     for i in range(len(counts)):
#         if counts[i]:
#             lst.append(i)
    
#     return lst

    


# result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
# print(result)

