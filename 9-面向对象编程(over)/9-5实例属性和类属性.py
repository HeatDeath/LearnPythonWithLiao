#由于Python是动态语言，根据类创建的实例可以任意绑定属性。

#给实例绑定属性的方法是通过实例变量，或者通过self变量：

class Student(object):
    def __init__(self,name):
        self.name=name

s=Student('Bob')
s.score=90

#但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：

class StudentX(object):
    name='StudentX'

s=StudentX()
print(s.name)
print(StudentX.name)
s.name='Michael'
print(s.name)
print(StudentX.name)
del s.name
print(s.name)


#从上面的例子可以看出，在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

#--------------------2017-2-16-15:35--------------