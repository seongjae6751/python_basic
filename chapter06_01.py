# Chapter06-1
# 파이썬 클래스
# OOP(객체 지향 프로그래밍), Self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 예제1
from unicodedata import name


class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age): #init은 class가 초기화 될때 호출되는 함수
        self.name = name
        self.age = age

# 클래스는 붕어빵 틀, 인스턴스는 틀을 가지고 찍어내는 객체
# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog("mikky", 2)
b = Dog("baby", 3)

# 비교
print(a == b, id(a), id(b))

# 네임스페이스
print('dog1', a.__dict__)
print('dog2', b.__dict__)

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

# 예제2
# self의 의미
class SelfTest:
    def func1(): # 클래스 안에서 구현된 함수를 메서드(method)라 함
        print('Func1 called')
    def func2(self):
        print('Func2 called')


f = SelfTest()

# print(dir(f))
print(id(f))
# f.func1() # 예외 # self 가 변수로 있어야지 호출 가능
f.func2() # 객체.메서드 형식 호출할때는 self를 생략해서 호출해야함
SelfTest.func1() 
# SelfTest.func2() 예외
SelfTest.func2(f) 

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0 # 재고
    def __init__(self, name):
        # 인스턴스 변수(암묵적으로 앞에 self가 붙은것)
        self.name = name 
        Warehouse.stock_num +=1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print()

print(Warehouse.stock_num)

print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num)

del user1
print('after', Warehouse.__dict__)

# 예제4
class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age): #init은 class가 초기화 될때 호출되는 함수
        self.name = name
        self.age = age
    
    def into(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return "{} is {}!".format(self.name, sound)

# 인스턴스 생성
c = Dog('July', 4)
d = Dog('Marry', 10)
# 메소드 호출
print(c.into())
# 메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))















    






