# 모듈 사용 실습

import sys

print(sys.path) # path는 경로를 보여줌

print(type(sys.path))

# 모듈 경로 삽입
# sys.path.append('C:/math')

# print(sys.path)

# import test_module

# 모듈 사용
# print(test_module.power(10,3))

import chapter06_02

import random 
a = 30 # 입력이 30이라고 가정
item_count = []
while len(item_count) < 31:
    item_count.append(0)
print("빈 리스트 : ", item_count) # 요소가 30개인 빈 리스트 생성.

while True :
        b = random.randint(0, a)
        item_count[b] += 1 # 숫자 n이 발생하면, n번째 자리에다가 카운트 +1
        break
print("카운트 한번 : ", item_count)

