
#------------列表生成器--------------

#列表生成式即List Comprehensions，
# 是Python内置的非常简单却强大的可以用来创建list的生成式。

#但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做?
#但是循环太繁琐，而列表生成式则可以用一行语句代替循
# 环生成上面的list：
print([x*x for x in range(1,11)])
#写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，
# 就可以把list创建出来。

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print([x*x for x in range(1,11) if x % 2== 0])
print([x*x for x in range(1,11) if x*x % 2== 0])
#两个式子效果相同

#还可以使用两层循环，可以生成全排列：
print([m+n for m in 'ABC' for n in 'XYZ'])

#for循环其实可以同时使用两个甚至多个变量，
# 比如dict的items()可以同时迭代key和value：
d={'x':'A','y':'B','z':'C'}
#字典(Dictionary)items()函数以列表返回可遍历的(键, 值)元组数组
for k,v in d.items():
    print(k,'=',v)

#因此，列表生成式也可以使用两个变量来生成list：
print([k+'='+v for k,v in d.items()])
print([k for k in d.items()])
print([k+v for k,v in d.items()])
print({k:v for k,v in d.items()})

#最后把一个list中所有的字符串变成小写：
L=['Hello','WORld','ApplLe','IBm']
print([s.lower() for s in L])
TL=['aplLE','piNApple','pEn']
print([x[0].upper()+x[1:].lower() for x in TL])


#---------------Practice--------------------

#如果list中既包含字符串，又包含整数，
# 由于非字符串类型没有lower()方法，所以列表生成式会报错：

#使用内建的isinstance函数可以判断一个变量是不是字符串：

#请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]
print(L2)



#------------------2017/02/12/10:51------------------