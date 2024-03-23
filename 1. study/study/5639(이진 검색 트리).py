import sys
sys.setrecursionlimit(10 ** 9)

# 완전 이진 트리가 아니네...
def postorder(s, e):
    if s > e:
        return
    mid = e + 1  # 오른쪽 노드가 없을 경우

    for i in range(s + 1, e + 1):
        if arr[s] < arr[i]:
            mid = i
            break

    postorder(s + 1, mid - 1)  # 왼쪽 확인
    postorder(mid, e)  # 오른쪽 확인
    print(arr[s])

arr = []
while True:
    try:
        temp = int(input())
        arr.append(temp)
    except:
        break

postorder(0, len(arr) - 1)


#왼쪽 자식 노드는 루트보다 작고,
# 오른쪽 자식노드는 루트보다 크다는 것을 이용해서
# 자식노드가 없는 노드부터 찾아서 하나씩 출력해주면 된다.