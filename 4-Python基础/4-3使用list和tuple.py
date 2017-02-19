
#--------------------list---------------------

#list是一种有序的集合，可以随时添加和删除其中的元素
classmate=['Mike','Bob','Tracy']
len(classmate)
print(len(classmate))

print(classmate[0])

#print(classmate[3])
'''
当索引超出了范围时，Python会报一个IndexError错误，
所以，要确保索引不要越界，记得最后一个元素的索引是
len(classmates) - 1。
'''

print(classmate[-1])

#print(classmate[-4])
#倒数第4个越界

#list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmate.append('Adam')
print(classmate)

#也可以把元素插入到指定的位置，比如索引号为1的位置
classmate.insert(1,'Jack')
print(classmate)

#要删除list末尾的元素，用pop()方法
classmate.pop()
print(classmate)

#要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmate.pop(1)
print(classmate)

#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmate[1]='Amy'
print(classmate)

#list里面的元素的数据类型也可以不同
L=['Apple',123,True]

#list元素也可以是另一个list
s=['a','b',L,'c']
print(s)
print(len(s))

#如果一个list中一个元素也没有，就是一个空的list，它的长度为0
L=[]
print(len(L))
print(L)

A=None
print(A)
A=[None]
print(A)

#--------------------tuple---------------------

#tuple和list非常类似，但是tuple一旦初始化就不能修改
classmate=('Mike','Bob','Tracy')

'''
现在，classmates这个tuple不能变了，它也没有append()，
insert()这样的方法。其他获取元素的方法和list是一样的，
你可以正常地使用classmates[0]，classmates[-1]，
但不能赋值成另外的元素。
'''

#tuple的陷阱：当你定义一个tuple时，在定义的时候，
# tuple的元素就必须被确定下来
t=(1,2)
print(t)

#如果要定义一个空的tuple，可以写成()
t=()
print(t)

#---!!!---
# 但是，要定义一个只有1个元素的tuple，如果你这么定义:
t=(1)
print(t)
'''
定义的不是tuple，而是1这个数！
这是因为括号()既可以表示tuple，
又可以表示数学公式中的小括号，这就产生了歧义，
因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
'''
#所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t=(1,)
print(t)
#Python在显示只有1个元素的tuple时，
# 也会加一个逗号,，以免你误解成数学计算意义上的括号。


#一个“可变”的tuple
t=('a','b',['c','d'])
print(t)
t[2][0]='f'
t[2][1]='g'
print(t)
print(len(t))
t[2].append('Mike')
print(t)
print(len(t))
'''
表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，
而是list的元素。tuple一开始指向的list并没有改成别的list，
所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，
但指向的这个list本身是可变的！
'''

#--------------------Practice---------------------
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

#----------------2017/02/10/14:58----------
