# Chapter03-6
# 집합(Set) 특징
# 집합(Set) 자료형(순서x, 중복x)
# list = [], tuple = (), dict = {}, set = {}, ([])

#선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.141592}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('b - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환(set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t -', t[0], t[1:3])

# 리스트 변환(set -> List)
l = list(c)
l2 = list(e)

print('l - ', l)
print('l2 - ', l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2: ', s1 & s2)
print('s1 & s2: ', s1.intersection(s2)) # 교집합
print('s1 | s2: ', s1 | s2)
print('s1 | s2: ', s1.union(s2)) # 합집합
print('s1 - s2: ', s1 - s2,)
print('s1 - s2: ', s1.difference(s2)) # 차집합

# is로 시작하는 함수는 false나 true 값을 리턴함.
# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2)) # False 일때 교집합이 있는거

# 부분 집합 확인
print('subset : ',s1.issubset(s2)) # 부분집합인가?
print('superset : ', s1.issuperset(s2)) # 확대집합인가?

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)
# s1.remove(7)

s1.discard(3)
print('s1 - ', s1)
# s1.discard(7) 예외가 발생x

s1.clear() # 리스트에서도 사용 가능
print('s1 - ', s1)

a = [1, 2, 3]
a.clear()
print(a)








