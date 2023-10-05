try:
    num = int(input('100으로 나눌 값을 입력해:'))
    print(100 / num)

except BaseException:
    print('숫자를 입력하라고')
except ZeroDivisionError:
    print('왜 0을 입력하는거야??, 너 수학 못하지?')

except:
    print('에러 발생')

# 0을 입력했을 때는 '왜 0을 입력하는거야??, 너 수학 못하지?'이게 나와야 하는데
# '숫자를 입력하라고' 이게 나옴