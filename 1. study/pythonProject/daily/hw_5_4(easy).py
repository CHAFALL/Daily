# main.py

# 아래 함수를 수정하시오.
def find_min_max(lst):
    
    lst_min = lst_max = lst[0]
    for ls in lst:
        if ls < lst_min:
            lst_min = ls
        if ls > lst_max:
            lst_max = ls

    return lst_min, lst_max
    

result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)