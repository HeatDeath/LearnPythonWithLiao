#正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：

class Student(object):
    pass

s=Student()

#然后，尝试给实例绑定一个属性：
s.name='Mike'
print(s.name)

#还可以尝试给实例绑定一个方法：

def setAge(self,age): #定义一个函数作为实例方法
    self.age=age

from types import MethodType
s.setAge=MethodType(setAge,s)  #给实例绑定一个方法
s.setAge(25)   #调用实例方法
print(s.age)



#但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2=Student()   # 创建新的实例
#s2.setAge(25)   # 尝试调用方法


#为了给所有实例都绑定方法，可以给class绑定方法：
def setScore(self,score):
    self.score=score

Student.setScore=setScore

#给class绑定方法后，所有实例均可调用：

s.setScore=(100)
#s.score     【有错误，但不知道错在哪里】




#------------------------使用__slots__-----------------

#但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class StudentX(object):
    __slots__=('name','age')

s=StudentX()
s.name='Mike'
s.age=25
#s.score=99

#由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。

#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

class GraduateStudent(StudentX):
    pass

g=GraduateStudent()
g.score=999


#-------------------2017-02-16--16:19-------------








