
'''
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，
列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，
不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，
那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。在
Python中，这种一边循环一边计算的机制，称为生成器：generator。

'''

#要创建一个generator，有很多种方法。
# 第一种方法很简单，只要把一个列表生成式的[]改成()，
# 就创建了一个generator：

L=[i for i in range(10)]
print(L)

g=(i for i in range(10))
print(g)

#创建L和g的区别仅在于最外层的[]和()，
# L是一个list，而g是一个generator。

#如果要一个一个打印出来，
# 可以通过next()函数获得generator的下一个返回值：
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#print(next(g))


'''
我们讲过，generator保存的是算法，每次调用next(g)，
就计算出g的下一个元素的值，直到计算到最后一个元素，
没有更多的元素时，抛出StopIteration的错误。
'''

#当然，上面这种不断调用next(g)实在是太变态了，
# 正确的方法是使用for循环，因为generator也是可迭代对象：
x=(x*x for x in range(10))
for i in x:
    print(i)

#所以，我们创建了一个generator后，基本上永远不会调用next()，
# 而是通过for循环来迭代它，并且不需要关心StopIteration的错误。

#斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：

def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n+=1
    return 'done'

max=input('input a number :')
fib(int(max))

'''
仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则
，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常
类似generator。

也就是说，上面的函数和generator仅一步之遥。
要把fib函数变成generator，只需要把print(b)改
为yield b就可以了：
'''

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield(b)
        a,b=b,a+b
        n+=1
    return 'done'

'''
但是用for循环调用generator时，发现拿不到generator的
return语句的返回值。如果想要拿到返回值，必须捕获
StopIteration错误，返回值包含在StopIteration的value中：

'''


#-------------practice-----------------
#杨辉三角定义如下：
'''
          1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
1   5   10  10  5   1
'''
n = 0


#参考i评论区的想法  :(
def triangles():
    L=[1]
    while True:
        yield L
        L.append(0)
        L=[L[i-1]+L[i] for i in range(len(L))]
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break