information = {}
authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
books = [
    ['장화홍련전', '가락국 신화', '온달 설화'],
    ['금오신화', '이생규장전', '만복자서포기'],
    ['수성지', '백호집', '원생몽유록'],
    ['홍길동전', '장생전', '도문대작'],
    ['옥루몽', '옥련몽'],
]

'''
- 작가와 작품 목록 참고
- 허균 : 홍길동전, 장생전, 도문대작
- 임제 : 수성지, 백호집, 원생몽유록
- 작자 미상 : 장화홍련전, 가락국 신화, 온달 설화
'''
# 방법1
# information[authors[0]] = books[1]
# information[authors[1]] = books[3]
# information[authors[2]] = books[4]
# information[authors[4]] = books[0]
# information[authors[5]] = books[2]
# 방법 2(개인적으로 난 이게 더 좋음)
informathon = {
    authors[0] : books[1],
    authors[1] : books[3],
    authors[2] : books[4],
    authors[3] : books[0],
    authors[4] : books[2]
    }

# # 방법 1 (비추) 이건 문제점이 0 1 2 3 4 에서 하나라도 없으면 안됨
# for i in range(len(informathon)):
#     print(f'{authors[i]} : {informathon[authors[i]]}')

# # 방법 2
# for key in informathon.keys():
#     print(f'{key} : {informathon[key]}')

# 방법 3
for key, value in informathon.items(): 
    print(f'{key} : {value}')

# # 방법 4 (비추)
# for x in range(len(informathon)):
#     print(f'{list(informathon.keys())[x]} : {list(informathon.values())[x]}')


#참고 print('\n') : 줄바꿈
#참고 print() : 줄바꿈
#참고 print('t') : tab