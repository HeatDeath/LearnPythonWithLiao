
#------------filter---------------

#Python内建的filter()函数用于过滤序列。

#和map()类似，filter()也接收一个函数和一个序列。
#和map()不同的是，filter()把传入的函数依次作用于每个元素
#然后根据返回值是True还是False决定保留还是丢弃该元素。

#例如，在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
    return n% 2==1
print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9,10])))

#把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()#没看懂
s=['A','b','c',None,'d','']
print(list(filter(not_empty,s)))

'''
not_empty()方法依次作用于s[]的每一个元素上
当遍历到 None 的时候，触发了else，返回值是Flase，该元素丢弃

当遍历到 ''的时候，触发了if条件，返回值为 s.strip() ，
即strip()方法作用在 字符串 '' 上， 字符串被移除了头尾指定的空格，
只剩下了None,以至于返回值也是Flase，该元素也被丢弃
'''
#参考了一下v2ex上的一个回答https://www.v2ex.com/t/299705
'''
Python 里
s and s.strip()
等同于
s.strip() if s else s
--------------------------
return s and s.strip()
就等同于
if s:
　　 return s.strip()
else:
　　 return s
'''
#注意到filter()函数返回的是一个Iterator，
# 也就是一个惰性序列，所以要强迫filter()完成计算结果，
# 需要用list()函数获得所有结果并返回list。


#--------------------practice-----------------
def is_palindrome(n):
    return str(n)==str(n)[::-1]
output = filter(is_palindrome, range(1, 1000))
print(list(output))

a='hello world'
print(a[::-1])