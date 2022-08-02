# Chapter03-3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서o, 중복o, 수정o, 삭제o)

# 선언
a = []
b = list()
c = [70, 75, 80, 85] #Len
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'footbar', 3, 4, False, 3.14159]
print()

# 인덱싱
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1], d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))
print()

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])
print()

# 리스트 연산
print('c + d', c + d)
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))
print()

# 값 비교
print(c == c[:3] + c [3:])
print()

# Identity(id)

temp = c
print(temp, c)
print(id(temp))
print(id(c))
print()

# 리스트 수정, 삭제
print('>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # [['a','b', 'c']]
print('c - ', c)
c[1] = ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[2]
print('c - ', c)
print()

# 리스트 함수
a =[5, 2, 3, 1, 4]

print('a - ', a)
a.append(10) # 맨 마지막 추가
print('a - ', a)
a.sort() # 크기 순으로 정렬
print('a - ', a)
a.reverse() # 거꾸로 뒤집기
print('a - ', a)
print('a - ', a.index(3)) #= a[3] # index는 위치 값
a.insert(2, 7) # a번째 위치에 삽입
print('a - ', a)
a.reverse()
print('a - ', a)
print()

# del a[9543]
a.remove(10) # 요소 바로 삭제
print('a - ', a)
print('a - ', a.pop()) # 맨 마지막 끄집어 내기
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4)) # 요소 개수 세주기
ex = [8,9]
a.extend(ex) # 리스트에 리스트 더하기
print('a - ', a)
print()

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)





