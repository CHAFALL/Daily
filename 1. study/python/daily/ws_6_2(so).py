# ws_6_2.py

# 아래 함수를 수정하시오.
def get_value_from_dict(my_dict, char):
    
    return my_dict.get(char)

my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result) # Alice
