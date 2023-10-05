# number_of_people = 0 #호출 근처에 두는 것을 권장

def increase_user():
    global number_of_people #여기 부분 주석처리하면 오류남(지역변수라도 주면 안남)
    print(f'현재 가입 된 유저 수: {number_of_people}')
    number_of_people += 1
    
# def increase_user():  #global을 쓰는 이유
#     number_of_people = 0
#     print(f'현재 가입 된 유저 수: {number_of_people}')
#     number_of_people += 1
    
#     return number_of_people


def create_user(name, age, address):
    # user_info = {}
    # user_info['name'] = name
    # user_info['age'] = age
    # user_info['address'] = address
    
    # 아래 방식도 가능함(이걸 더 추천)
    user_info = {
        'name': name,
        'age': age,
        'address' : address,
    }
    
    increase_user()
    print(f'{name}님 환영합니다!')
    
    return user_info

number_of_people = 0

# define 하고 아래로 2줄 띄우고 하는 걸 권장
result = create_user('홍길동', 30, '서울')
print(result)
print(f'현재 가입 된 유저 수: {number_of_people}')
