# 1. 절댓값을 반환하는 함수 abs를 사용하여 아래 변수에 담긴 값의 절댓값을 출력하시오.
negative = abs(-3)


# 2. 아래 변수에 담긴 값의 boolean 값을 출력하시오.
empty_list = bool([])


# 3. 주어진 리스트가 가진 모든 값을 더한 결과를 출력하시오.
my_list = [1, 2, 3, 4, 5]
total = sum(my_list)

# 4. 주어진 정렬을 오름차순으로 정렬한 결과를 출력하시오.
unsorted_list = ['하', '교', '캅', '의', '지', '가']

sorted_list = sorted(unsorted_list) #비파괴 함수, 리턴값 받아줘야됨
print(sorted_list)
# unsorted_list.sort() #파괴 메서드

print(negative)
print(empty_list)
print(total)
print(sorted_list)
# print(unsorted_list)
