
#既然变量可以指向函数，函数的参数能接收变量，
# 那么一个函数就可以接收另一个函数作为参数，
# 这种函数就称之为高阶函数。

#--------------------map----------------------

#map()函数接收两个参数，一个是函数，一个是Iterable，（可迭代对象）
# map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的Iterator返回。

#比如我们有一个函数f(x)=x2，
# 要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，
# 就可以用map()实现如下：
def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
#【？？】list函数是啥玩意？？？
print(list(r))
#map()传入的第一个参数是f，即函数对象本身。
# 由于结果r是一个Iterator，Iterator是惰性序列，
# 因此通过list()函数让它把整个序列都计算出来并返回一个list。

a=123
#【？？】str函数又是啥玩意？？？
b=str(a)
print(list(b))

#map()作为高阶函数，事实上它把运算规则抽象了，
#还可以计算任意复杂的函数
print(list(map(str,[1,2,3,4,5,6,7,8,9])))

#-----------------------------reduce------------------------

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[1,3,5,7]))

#但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场
def fn(x,y):
    return x*10+y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#【？】char2num函数的作用是将list中字符串中的数字转换为数字
print(list(map(char2num,'13579')))
print(list(map(char2num,['1','3','5','7','9'])))
print(reduce(fn,map(char2num,'13579')))

#整理成一个str2int的函数就是：
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(char2num,s))
print(str2int('13579'))

#还可以用lambda函数进一步简化成：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))

#----------------一点思考---------------
a='xyz'
b='x''y''z'
c='x','y','z'
print(a)# a是一个str
print(b)# b是一个str
print(c)# c是一个拥有3个str的tuple

d=['x','y','z']
e=['x''y''z']
h=['xyz']
print(d)# d是一个拥有3个str的list
print(e)# e是一个拥有1个str的list
print(h)# h是一个拥有1个str的list

f=('x','y','z')
g=('x''y''z')
i=('xyz')
print(f)# f是一个拥有3个str的tuple
print(g)# g是一个str
print(i)# i是一个str
#--------------------------------------

#----------------Practice【1】---------------
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
# 其他小写的规范名字。输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart']：

#【方法一】
def normalize(name):
    def FirstLetterUpper(a):
        return a[:1].upper()+a[1:].lower()
    return list(map(FirstLetterUpper,name))
print(normalize(['MikE','jack','tOMy']))
#【解析】
#传入FirstLetterUpper函数的参数a是名为name的list中的一个元素

test_a='abc'
print(test_a[0])

#【方法二】
def normalizeX(name):
    def FirstLetterUpperX(a):
        return a.capitalize()
    return list(map(FirstLetterUpperX,name))
print(normalizeX(['MikE','jack','tOMy']))
#【解析】
#capitalize()将字符串的第一个字母变成大写,其他字母变小写

#----------------Practice【2】---------------

#Python提供的sum()函数可以接受一个list并求和，
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def prod(L):
    return reduce(lambda x,y:x*y,L)
print(prod([2,4,5,6,7]))

def prodX(L):
    def mul(x,y):
        return x*y
    return reduce(mul,L)
print(prod([2,4,5,6,7]))


#----------------Practice【3】---------------

#利用map和reduce编写一个str2float函数，
# 把字符串'123.456'转换成浮点数123.456：


#廖雪峰github上的答案。复杂难懂（没看懂
char2float={'.':-1 , '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(ss):
    nums=list(map(lambda ch:char2float[ch],ss))
    point=0
    def tofloat(f,n):
        nonlocal point
        if n==-1:
            point=1
            return f
        if point==0:
            return f*10+n
        else:
            point*=10
            return f+n/point
    return reduce(tofloat,nums,0.0)
print(str2float('123.56'))

#另一个评论区中非常【棒！！！】的答案
def str2floatX(s):
    L=list(map(int,s.split('.')))
    return reduce(lambda x,y:x+y*0.1**len(str(y)),L)
print(str2floatX('123.56'))
'''
【解析】
s.split将'123.56'从'.'分为'123'和'56'两个字符串
list(map(int,s.split('.')))将'123.56'这个
str转换为名为L的list，L=[123,56]
123+56*01^2=123.56
'''



text_fff=[1,2,3,4,5,6,7,8,9,11]
print(len(text_fff[5:]))

#-----------2017/02/10/22:04---------------