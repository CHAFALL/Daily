# class Person:
#     def __init__(self, name, age, number, email):
#         self.name = name
#         self.age = age
#         self.number = number
#         self.email = email
        
# class Student(Person):
#     # def __init__(self, name, age, number, email,student_id):
#     #     super().__init__(name, age, number, email)
#     #     self.student_id = student_id
#     pass   #이렇게 해도 돌아감, 여기에 없으면 상위 클래스에서 찾음
        
# s1 = Student ('김학생', 24, 1, 'kim@ssafy.com')

#except
# try:
#     num = int(input())
#     result = 10/ num

# except ZeroDivisionError:
#     print('0으로 나눌 수 X')
    
# except ValueError:
#     print('숫자를 넣어주세요')

# except:
#     print('에러 발생')

try:
    num = int(input())
    result = 10/ num

except Exception:
    print('입력 다시 확인 필요')