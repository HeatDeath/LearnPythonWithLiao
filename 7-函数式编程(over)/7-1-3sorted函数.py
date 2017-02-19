
#Python内置的sorted()函数就可以对list进行排序：
a=[2,3,4,5,1,2,22,6,55,-8]
b=sorted(a)
#默认从小到大排列
print(b)

#此外，sorted()函数也是一个高阶函数，
# 它还可以接收一个key函数来实现自定义的排序，
# 例如按绝对值大小排序：
c=sorted(a,key=abs)
print(c)
#key指定的函数将作用于list的每一个元素上，
# 并根据key函数返回的结果进行排序。
# 对比原始的list和经过key=abs处理过的list：
#然后sorted()函数按照keys进行排序，
# 并按照对应关系返回list相应的元素：


#我们再看一个字符串排序的例子：
d=sorted(['bob','kack','daming','Lingling','Amy'])
print(d)
#默认情况下，对字符串排序，是按照ASCII的大小比较的，
# 由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。

#现在，我们提出排序应该忽略大小写，按照字母序排序。
# 要实现这个算法，不必对现有代码大加改动，
# 只要我们能用一个key函数把字符串映射为忽略大小写排序即可。
# 忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写
# （或者都变成小写），再比较。


#这样，我们给sorted传入key函数，即可实现忽略大小写的排序：
e=sorted(d,key=str.lower)
print(e)


#要进行反向排序，不必改动key函数，
# 可以传入第三个参数reverse=True：
f=sorted(e,key=str.lower,reverse=True)
print(f)

#假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：
print(sorted(L,key=lambda x:x[0]))

#再按成绩从高到低排序：
print(sorted(L,key=lambda x:x[1],reverse=True))














