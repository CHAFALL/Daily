# # 16진수를 10진수로 입력받기
# num = int(input(), 16)
# print(num) # 십진수
# # 16진수로 출력 하기
# print(f'{num:x}') # 16진수 소문자
# print(f'{num:+X}') # 16진수 대문자 + 부호까지
# print(f'{num:b}') # 2진수 소문자
# print(f'{num:o}') # 8진수 소문자
#
# print(f'{num:<16b}')
# print(f'{num:>16b}')
# print(f'{num:^16b}')
#
# print(5 ^ 3) # (비트연산 xor) # 6


#xor 연습(시험 각이다)
a = 0x86
key = 0xAA # 암호화 key or 복호화 key가 될 수 있다.
print(f'{a:d}') # 10진수
print(f'{a:X}') # 16진수
print(f'{a:b}')
print(f'{key:b}')
a = a ^ key
# print(f'{a:8b}')
print(f'{a:08b}')  # 필요없는 0 붙이는 방법

print(f'{a:d}') # 10진수
print(f'{a:X}') # 16진수


a = a ^ key
print(f'{a:08b}')
print(f'{a:d}') # 10진수
print(f'{a:X}') # 16진수