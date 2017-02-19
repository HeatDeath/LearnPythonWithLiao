#Python的functools模块提供了很多有用的功能，
# 其中一个就是偏函数（Partial function）。
# 要注意，这里的偏函数和数学意义上的偏函数不一样。

#int()函数可以把字符串转换为整数，当仅传入字符串时，
# int()函数默认按十进制转换：

print(int('12345'))

#但int()函数还提供额外的base参数，默认值为10。
# 如果传入base参数，就可以做N进制的转换：

print(int('12345',base=8))
print(int('12345',base=16))
print('-----------------------')

#假设要转换大量的二进制字符串，
# 每次都传入int(x, base=2)非常麻烦，
# 于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：

def int2(x,base=2):
    return int(x,base)

print(int2('1000000'))


#functools.partial就是帮助我们创建一个偏函数的，
# 不需要我们自己定义int2()，可以直接使用下面的代码
# 创建一个新的函数int2：

import functools
int3=functools.partial(int,base=2)
print(int3('101010101010101'))

#所以，简单总结functools.partial的作用就是，
# 把一个函数的某些参数给固定住（也就是设置默认值）
# 返回一个新的函数，调用这个新函数会更简单。


'''
当函数的参数个数太多，需要简化时，使用
functools.partial可以创建一个新的函数，
这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
'''







