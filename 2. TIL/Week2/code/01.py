# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def talk(self):
#         print(f'안녕, {self.name}입니다.')
        
# class Professor(Person):
#     def __init__(self, name, age, department):
#         self.name = name
#         self.age = age
#         self.department = department

# class Student(Person):
#     def __init__(self, name, age, gpa):
#         self.name = name
#         self.age = age
#         self.gpa = gpa
        
# p1 = Professor('박교수', 40, '컴공')
# s1 = Student ('김학생', 20, 3.5)

# p1.talk()
# s1.talk()
# #```````````````````````````````````````````````````
# # self.name = name
# # self.age = age
# # 은 다 중복 되니 빼고 작성하고 싶다!  

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def talk(self):
#         print(f'안녕, {self.name}입니다.')
        
# class Professor(Person):
#     def __init__(self, name, age, department):
#         # Person.__init__(self, name, age) #단 유연함 떨어짐, Person이라는 클래스의 이름이 바뀐다면 일일이 바꿔줘야함
#         super().__init__(name, age) #super 이용
#         self.department = department

# class Student(Person): #class Student(Person, aaa ,aa):다중상속, 중복되는 것이 있을 수 있는데 인자 표기 순서 순으로 처리해줌
#     def __init__(self, name, age, gpa):
#         super().__init__(name, age)
#         self.gpa = gpa
        
# p1 = Professor('박교수', 40, '컴공')
# s1 = Student ('김학생', 20, 3.5)

# p1.talk()
# s1.talk()
                
#다중상속
class Person:
    gene = 'XYZ'
    
    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        print(f'안녕, {self.name}입니다.')
        
    
       
class Mom(Person):
    gene = 'XX'

    def __init__(self, name):
        super().__init__(name) #이거 안 써도 되긴하는 데 쓰는 게 맞음(정석)
    
    def swim(self):
        return '엄마가 수영'
    
class Dad(Person):
    gene = 'XY'

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def walk(self):
        return '아빠가 걷기'
        
class FirstChild(Dad, Mom):
    
    mom_gene = Mom.gene #상속 순서는 바꾸기 그런데 엄마 유전자를 뽑고 싶을 때(이 방법 뿐임)
    
    def __init__(self, name, age):
        # super().__init__(name)
        Dad.__init__(self, name , age) #Dad 것의 초기값을 받아오고 싶을 때 
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'
    

baby1 = FirstChild('아가')
print(baby1.cry()) #첫째가 응애
print(baby1.swim()) #첫째가 수영
print(baby1.walk()) #아빠가 걷기 #상위로 찾아서 들어감
print(baby1.gene) # XY 두개가 겹쳤는데 Dad를 Mom보다 먼저 썻으므로 XY가 나옴

print(FirstChild.mro()) #속성이건 메소드 건 찾아올라가는 순서이다.
# print(baby1.mom_gene) #이렇게 유전자 가져옴 (이 방법 뿐임)

