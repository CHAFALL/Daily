# ws_5_5.py

# 아래 함수를 수정하시오.
def even_elements(lst):
    new_my_list = []
    while lst: #pop 사용시 리스트에 변화가 일어나는 것을 조심
        
        pop_l = lst.pop(0)
        if pop_l % 2 == 0:
            new_my_list.extend([pop_l])

    return new_my_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)