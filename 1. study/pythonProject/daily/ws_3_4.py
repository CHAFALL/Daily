
def create_user(name, age, address):
     
    user_list = {
        'name' : name,
        'age' : age,
        'address' : address
    }
    print(f'{name}님 환영합니다!')
    
    return user_list

name_list=['김시습', '허균', '남영로', '임제', '박지원']
age_list = [20, 16, 52, 36, 60]
address_list = ['서울', '강릉', '조선', '나주', '한성부']


total_user_list = list(map(create_user, name_list, age_list, address_list))

print(total_user_list)
     

