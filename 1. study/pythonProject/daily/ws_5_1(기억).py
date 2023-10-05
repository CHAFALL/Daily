# ws_5_1.py

# 아래 함수를 수정하시오.
# def reverse_string(chars):              #기억하기!!!!
#     new_chars = ''
#     for reverse_char in reversed(chars):
#         new_chars += reverse_char
    
#     return new_chars


# result = reverse_string("Hello, World!")
# print(result)
#`````````````````````````````````````````````````````````````
def reverse_string(chars):              #기억하기!!!!
    
    new_chars_list = list(reversed(chars)) #객체 꼴로 나오면 그냥 리스트하고 join 시키기!!
    new_chars = ''.join(new_chars_list) 
    
    return new_chars


result = reverse_string("Hello, World!")
print(result)


#------------------------------------------------------------

# def reverse_string(chars):              
#     new_chars = chars[::-1]
#     # print(chars) # Hello, World! 리턴값 필요하네
#     return new_chars


# result = reverse_string("Hello, World!")
# print(result)

#---------------------------------------------------------

#문자열은 reverse() 함수란 것이 없음(문자열은 불변이자너)
# def reverse_string(chars):
#     chars_list = list(chars)
#     chars_list.reverse()
#     reverse_chars = ''.join(chars_list)

#     return reverse_chars

# result = reverse_string("Hello, World!")
# print(result)



