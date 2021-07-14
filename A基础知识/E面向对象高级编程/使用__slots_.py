from A基础知识.D面向对象.实例属性与类属性 import Student

s1 = Student('老司机')


def didi():
    print('GuaGuaGua...')


# 给实例增加一个方法
s1.gua = didi
s1.gua()

s2 = Student('公交车司机')


# 会报错，因为gua方法只属于s1那个实例
# s2.gua()


# 为了给所有实例都绑定方法->则将该方法绑定到class上，动态得给class增加一个方法
# 给class绑定方法与给实例绑定方法有一点极为不同的地方是，给class绑定的方法一定要有一个self形参，否则会报错
def didi2(self):
    print("Gua2...")


Student.gua = didi2
s2.gua()


# 使用__slots__如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

# >>> s = Student() # 创建新的实例
# >>> s.name = 'Michael' # 绑定属性'name'
# >>> s.age = 25 # 绑定属性'age'
# >>> s.score = 99 # 绑定属性'score'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'score'
