# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용(JSON)
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

#선언
from setuptools import SetuptoolsDeprecationWarning


a = {'name': 'kim', 'phone': '01044076751', 'birth': '001111'}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(
    Name='Niceman',
    City='Seoul',
    Age=33,
    Grade='A',
    Status=True
) # 가장 추천

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 출력
print('a - ', a['name']) # 존재x -> 에러발생
print('a - ', a.get('name')) # 존재x -> None 처리
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# 딕셔너리 추가
a['adress'] = 'seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

#딕셔너리 길이
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# dict_key, dict_value, dict_items : 반복문(__iter__)에서 사용가능

print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print('a - ', list(a.keys()))
print('b - ', list(b.keys()))
print()

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print('a - ', list(a.values()))
print('b - ', list(b.values()))
print()

print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())

print('a - ', list(a.items()))
print('b - ', list(b.items()))
print()

print('a - ', a.pop('name'))
print('a - ', a)
print('a - ', c.pop('arr'))
print('a - ', c)
print()

print('f - ', f.popitem()) # 추첨기
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print()

print('a - ', 'birth2' in a)
print('a - ', 'City' in d)

# 수정
a['test'] = 'test_dict'

print('a - ', a)

a['adress'] = 'dj'
print('a - ', a)

a.update(birth='001112') # 문법적으로 확실
print('a - ', a)
temp = {'adress': 'Busan'}

a.update(temp)
print('a - ', a)











