import matplotlib.pyplot as plt

# 예제 1: x, y가 같을 때
plt.plot([1,2,3,4])
# plt.show() # 이거 주석처리하면 예제 1번이랑 예제 2번이 중접되어서 나옴

# 참고: 이때까지 그렸던 plot 지우기
plt.clf()

# 되도록이면 x축은 통일화 하기!!!(원치 않는 그림이 나올 수 있다, 정렬? 관련 문제)

# 예제 2: x, y가 다를 때
x = [1, 2, 3, 4]
y = [2, 4, 8, 16]
plt.plot(x, y)
# plt.show()
plt.clf()
# 예제 3: 제목 + 각 축의 설명
plt.plot(x, y)
# 제목
plt.title("Test Graph")

# x, y축
plt.ylabel('y label')
plt.xlabel('x label')

# plt.show() # 출력하는 순간 다 삭제가 되므로 show를 지워줘야 된다.

# 파일로 저장하기
plt.savefig('filename.png')