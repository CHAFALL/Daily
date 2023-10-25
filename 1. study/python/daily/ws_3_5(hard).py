
def decrease_book(number):
    global number_of_book
    number_of_book-=number
    print(f'남은 책의 수 : {number_of_book}')


def create_user(name, age, address):
    user_list = {} #이거 까먹지 말것
    user_list['name'] = name
    user_list['age'] = age
    user_list['adress'] = address
    print(f'{name}님 환영합니다.')
    return user_list

def rental_book(info): #왜 for문도 안 썻는데 촥촥촥 하나씩 들어가지?
    name = info['name'] #내가 볼땐 맨 밑에 쓴 map함수 때문에 그런듯
    age = info['age//10']
    decrease_book(age)
    print(f'{name}님이 {age}권의 책을 대여하였습니다.')
    


number_of_book = 100

name_list=['김시습', '허균', '남영로', '임제', '박지원']
age_list = [20, 16, 52, 36, 60]
address_list = ['서울', '강릉', '조선', '나주', '한성부']

many_user = list(map(create_user, name_list, age_list, address_list))
info = list(map(lambda x: {'name' : x['name'], 'age//10' : x['age']//10}, many_user)) 

#[{'name': '김시습', 'age//10': 2}, {'name': '허균', 'age//10': 1}, {'name': '남영로', 'age//10': 5}, {'name': '임제', 'age//10': 3}, {'name': '박지원', 'age//10': 6}]

# def info_test(x): #위의 것 풀어쓴 것
#     return {
#         'name' : x['name'],
#         'age//10' : x['age']//10
#     }

list(map(rental_book, info))


