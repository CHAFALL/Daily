# 비트 마스킹

visited1 = [1, 0, 0, 0, 1] # 0, 4번 방문
visited2 = 0b10001
print(visited2)
######################################################
visited = 0
# 원소 추가
visited = visited | 1 << 3
print(visited, bin(visited)) # 8 0b1000

# 원소 제거
visited = visited & ~(1 << 3) # 01001000 과 11110111 and 한 느낌(딴 거 0이면 그것도 0되어버리므로)
print(visited, bin(visited)) # 0 0b0

# 원소 조회
visited = visited | 1 << 3
print(visited & (1 << 3)) # 8
visited = visited & ~(1 << 3)
print(visited & (1 << 3)) # 0

# 원소 토글
visited = visited ^ (1<<3)
print(visited, bin(visited)) # 8 0b1000
visited = visited ^ (1<<3)
print(visited, bin(visited)) # 0 0b0
visited = visited ^ (1<<3)
print(visited, bin(visited)) # 8 0b1000

