import types

from 面向对象.类与实例与访问限制 import Student
from 面向对象.继承与多态 import Animal

### type函数返回对应的Class类型

print(type(123))
print(type(12.3))
print(type('123'))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({1, 2, 3, 1}))
print(type({1: 2, 2: 3, 3: 23, 1: 123}))

# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'list'>
# <class 'tuple'>
# <class 'set'>
# <class 'dict'>

print(type(abs))

# <class 'builtin_function_or_method'>

animal = Animal()
print(type(animal))
# <class 'D面向对象.继承与多态.Animal'>

# types模块中定义了常量
print(type(123) == type('123'))

# 注意：abs属于内置函数types.BuiltinFunctionType
print(type(abs) == types.BuiltinFunctionType)
print(type(abs) == types.FunctionType)

### isinstance()函数,判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
### 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
s1 = Student('taoGe', 18)
print(s1.__dir__())
