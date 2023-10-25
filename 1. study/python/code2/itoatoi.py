# str() 구현하기
def itoa(num):
    s = ''
    while num > 0:
        temp = num % 10
        s += chr(ord('0') + temp)
        num = num // 10

        #뒤집기(거꾸로 나오므로)
        s_list = list(s)
        N = len(s_list)
        for i in range(N // 2):
            s_list[i], s_list[N-1-i] = s_list[N-1-i], s_list[i]

    return ''.join(s_list)

number = 123
print(itoa(number), type(itoa(number)))
#-------------------------------------------------------------------------------

#int() 구현하기
def atoi(char):
    num = 0
    for i in range(len(char)):
        num = num * 10 + ord(char[i]) - ord('0')

    return num


char = '123'
print(atoi(char), type(atoi(char)))

