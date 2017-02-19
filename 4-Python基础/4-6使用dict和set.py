
#--------------------dict---------------------

#Python内置了字典：dict的支持，dict全称dictionary，
# 在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d={'Mike':95,'Bob':75,'Tracy':97}
print(d['Mike'])
#print(d[95])  无法使用value来查找key

#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
d['Adam']=67
print(d)

#由于一个key只能对应一个value，所以，多次对一个key放入value，
# 后面的值会把前面的值冲掉
d['Jack']=90
print(d)
d['Jack']=69
print(d)

#如果key不存在，dict就会报错
#print(d['Daming'])

#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Daming' in d)

#二是通过dict提供的get方法，如果key不存在，可以返回None，
# 或者自己指定的value：
print(d.get('Daming'))
print(d.get('Daming',-666))

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Mike')
print(d)
#d.pop(key)的返回值为key所对应的value
print(d.pop('Bob'))
print(d)

#请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
'''
和list比较，dict有以下几个特点：
    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。
而list相反：
    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。
    所以，dict是用空间来换取时间的一种方法。
'''

'''
dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，
正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出
的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法
称为哈希算法（Hash）。
要保证hash的正确性，作为key的对象就不能变。在Python中，
字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，
就不能作为key：
'''

#--------------------set---------------------

#set和dict类似，也是一组key的集合，但不存储value。
# 由于key不能重复，所以，在set中，没有重复的key。

#要创建一个set，需要提供一个list作为输入集合：
s=set([1,2,3])
print(s)

#注意，传入的参数[1, 2, 3]是一个list，
# 而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，
# 显示的顺序也不表示set是有序的。
#重复元素在set中自动被过滤：
s=set([1,1,1,2,2,2,3,2,3,4,1])
print(s)

#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(6)
print(s)

#通过remove(key)方法可以删除元素：
s.remove(2)
print(s)

#set可以看成数学意义上的无序和无重复元素的集合，
# 因此，两个set可以做数学意义上的交集、并集等操作：
s1=set([1,2,3])
s2=set([5,4,2])
print(s1&s2)
print(s1|s2)
'''
set和dict的唯一区别仅在于没有存储对应的value，
但是，set的原理和dict一样，所以，同样不可以放入可变对象，
因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
试试把list放入set，看看是否会报错。  【会报错！！】
'''
print(s1)
s1.add(99)
print(s1)


#--------------------再议不可变对象---------------------

#str是不变对象，而list是可变对象
#对于可变对象，对list进行操作，list内部的内容是会变化的，比如
a=['c','b','a']
print(a)
a.sort()
print(a)

#而对于不可变对象，比如str，对str进行操作呢：
a='abc'
b=a.replace('a','A')
print(a)
print(b)
'''
所以，对于不变对象来说，调用对象自身的任意方法，
也不会改变该对象自身的内容。
相反，这些方法会创建新的对象并返回，
这样，就保证了不可变对象本身永远是不可变的。
'''


#--------------2017/02/10/15:58-----------------