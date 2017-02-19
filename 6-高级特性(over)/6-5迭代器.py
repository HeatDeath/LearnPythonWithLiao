'''
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

Python的for循环本质上就是通过不断调用next()函数实现的
'''

'''
生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

把list、dict、str等Iterable变成Iterator可以使用iter()函数
'''

'''
因为Python的Iterator对象表示的是一个数据流，Iterator对象可以
被next()函数调用并不断返回下一个数据，直到没有数据时
抛出StopIteration错误。可以把这个数据流看做是一个有序序列
，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按
需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回
下一个数据时它才会计算。

Iterator甚至可以表示一个无限大的数据流，例如全体自然数。
而使用list是永远不可能存储全体自然数的。
'''


#---------------2017/02/15---------------