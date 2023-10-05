try:
    num = int(input('100으로 나눌 값을 입력해:'))
    print(100 / num)

except ValueError:
    print('숫자를 입력하라고')
except ZeroDivisionError:
    print('왜 0을 입력하는거야??, 너 수학 못하지?')

# except (ValueError,ZeroDivisionError):
#     print('이렇게 묶어서 할 수도 있음')

except:
    print('에러 발생')

# except도 순서대로 작동함(except 작성순), 그래서 주의할 점 있음(아래의 블록에 도달하지 못할 수 있음)
# 그래서 하위 클래스 먼저 써 줘야함