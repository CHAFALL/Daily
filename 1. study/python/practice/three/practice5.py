# 0 ~ 9
# make set - 집합을 만들어 주는 과정
# 각 요소가 가리키는 값이 부모
parent = [i for i in range(10)]

# find - set
def find_set(x):
    if parent[x] == x:
        return x
    # else:
    # return find_set(parent[x])

    # 경로 압축
    # 내가 지금 가지고 있는 부모를 대표자로 고쳐줌
    parent[x] = find_set(parent[x])
    return parent[x]

# union
def union(x, y):
    # 1. 이미 같은 집합인 지 체크
    x = find_set(x)
    y = find_set(y)

    # 대표자가 같으니, 같은 집합이다.
    if x == y:
        # 이미 같은 집합이니 아무런 동작 필요 x

        # 싸이클 판단 하기(내일 내용)
        # print("싸이클 발생")
        return

    # 2. 다른 집합이라면, 같은 대표자로 수정
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

    # cf) 아래와 같이만 해도 되지만 통일성을 위해서.. 위와 같이 (다 작은 것만 가리키도록)
    # arent[y] = x

union(0, 1)
union(2, 3)
union(1, 3)
# 이미 같은 집합에 속해 있는 원소를 한 번 더 union
# 싸이클이 발생
union(0, 2)
# 대표자 검색
print(find_set(2)) # 0
print(find_set(3)) # 0

# 같은 그룹인 지 판별
t_x = 0
t_y = 2

if find_set(t_x) == find_set(t_y):
    print(f'{t_x} 와 {t_y} 는 같은 집합에 속해 있습니다.')
else:
    print(f'{t_x} 와 {t_y} 는 다른 집합에 속해 있습니다.')

# 내일 내용!!
# 같은 집합에 있는 걸 안다고 뭐가 좋을까? 싸이클 발생을 체크 가능!
# 이러면 싸이클이 발생 여부에 따라 연결할 지 말지 결정도 가능