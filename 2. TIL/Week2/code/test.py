# my_set = {2, 1, 3}
# # my_set.discard(2)

# # print(my_set)

# # print(my_set.discard(10))
# # #my_set.remove(10)

# element = my_set.pop()
# print(element)
# print(my_set)



# my_dict = {'name': '홍길동'}

# print(my_dict['name'])
# print(my_dict.get('name'))

# # print(my_dict['age']) # keyError
# print(my_dict.get('age')) # None
# print(my_dict.get('age', 'Unknown')) # Unknoun


# person = {'name': '홍길동', 'age' : 25}
# print(person.keys()) #dict_keys(['name', 'age'])
# for key in person.keys():
#     print(key) #name
#                #age
    
# print(person.values()) #dict_values(['홍길동', 25])
# for value in person.values():
#     print(value) #홍길동
#                  #25
# print(person.items()) #dict_items([('name', '홍길동'), ('age', 25)])
# for key ,value in person.items(): 
#     print(key, value) #name 홍길동
#                       #age 25
    
    
    
    
    
# 혈액형 인원수 세기
# 결과 => {'A': 3, 'B': 3, 'O' : 3,'AB' : 3}
blood_types = ['A', 'B' ,'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

# []
new_dict = {}
# blood_types을 순회하면서
for blood_type in blood_types:
    # 기존에 키가 이미 존재한다면,
    if blood_type in new_dict:
        #기존에 키의 값을 +1 증가
        new_dict[blood_type] +=1
        #키가 존재하지 않는다면 (처음 설정되는 키)
    else:
        new_dict[blood_type] = 1
print(new_dict)

# .get
new_dict = {}
# blood_types을 순회하면서
for blood_type in blood_types:
    new_dict[blood_type] = new_dict.get(blood_type, 0) +1
print(new_dict)

# .setdefault()
new_dict = {}
for blood_type in blood_types:
    
    new_dict.setdefault(blood_type, 0)
    new_dict[blood_type]+= 1
print(new_dict)


# a = [1, 2, 3]
# #슬라이싱
# b= a[:]
# b[0] = 100 
# print(a, b) #[1, 2, 3] [100, 2, 3]

# #copy
# c= a.copy()
# c[0] = 100
# print(a, c) #[1, 2, 3] [100, 2, 3]

# # 얕은 복사의 한계
# # 가장 큰 리스트는 복사가 되었는데 그 속의 리스트는 따로 복사가 되지 않아서 같은 곳을 보고 있어 함께 변경됨
# a = [1, 2, [1,2]]

# b= a[:]
# b[2][0] = 999
# print(a, b) #[1, 2, [999, 2]] [1, 2, [999, 2]]

# a = [1, 2, [1,2]]

# b= a.copy()
# b[2][0] = 999
# print(a, b) #[1, 2, [999, 2]] [1, 2, [999, 2]]

# #깊은 복사
# import copy
# original_list = [1, 2, [1,2]]

# deep_copied_list = copy.deepcopy(original_list)

# deep_copied_list[2][0] = 999
# print(original_list, deep_copied_list) #[1, 2, [1, 2]] [1, 2, [999, 2]]


