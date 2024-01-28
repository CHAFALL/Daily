N = int(input())
item = []
for _ in range(N):
    item.append(int(input()))
item.sort(reverse=True)

total = 0
# 3번째 마다 띄어넘기
for i in range(1, N + 1):
    if i % 3 == 0:
        continue
    total += item[i - 1]

print(total)
