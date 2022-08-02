#chapter_02-1
#파이썬 완전 기초
#프린트 사용법
# 참조 : https://www.python-course.eu/python3_formatted_output.php

#기본출력
print('python start')
print("python start")
print()
print('''python start''')

#separator 옵션
print('p','y','t','o','n', sep='1')
print('010','7777','1234', sep='-')
print('python' , 'google.com', sep='@')


print()

#end 옵션

print('welcome to', end='    ')
print('IT News' , end=' ')
print('Web Site')
print()

#file 옵션
import sys
print('Learn Python', file=sys.stdout)

#format 사용(d : 3 , s : 'python' , f : 3.1445454)
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one','two')) # format에는 {} 만 사용가능
print('{1} {0}'.format('one', 'two'))

print( )

# %s
print('%10s' % ('nice111'))
print('{:>10}'.format('nice'))

print('%-10s' % ('nice111'))
print('{:10}'.format('nice'))

print('{:*>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%5s' % ('python study'))
print('%.5s' % ('python study'))

print('{:10.8}'.format('python study'))

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (43))
print('%4d' % (4324556))
print('{:4d}'.format(42)) # 정수일때는 % 뒤에 d필요


# %f

print('%f' % (3.144334545454545))
print('{:f}'.format(3.144334545454545))

print('%06.2f' % (3.14592653589793) )
print('{:06.2f}'.format(3.14592653589793))
 
#구구단
for i in range(2, 10):
    for j in range(1, 10):
        print((i * j), end=' ')
    print()

