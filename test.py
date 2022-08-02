#cp02-01
from operator import truediv
from xmlrpc.server import list_public_methods


print('{:5d}'.format(32))
print('{:2.1s}'.format('python study'))
print('welcome to', end='99')
print('IT News' , end=' ')
print('Web Site')
print('{0} {2} {1}'.format('one', 'two', 'three'))
print('{:05.6f}'.format(3.14592653589793))

#cp02-02
print(int(300.5))

#cp03-1
i = 656687878788773333333333333333322222
print(i)
a = divmod(100, 8)
print(a)
c = 4
d = 5
print("b", c*d)
bool = True
print(type(bool))
print(divmod(100,8))

#cp03-2
str_o1 = "python"
print('a \n b')
print(type(003.14))
str_o1 = "seong jae"
# x print("sorted :", str_o1.sorted())
# x print("Capialize: ", capitalize(str_o1))

#cp04-2
for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i * j), end='')

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 24:
        print("Found : 24")
        break
    else:
        print('Not found : 24')

sum1 = 0
for v in range(1, 1001):
    sum1 = sum1 + v

print(sum1)

