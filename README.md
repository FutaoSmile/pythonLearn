# pythonLearn
学习python
https://www.liaoxuefeng.com/wiki/1016959663602400/1017317609699776
	
* Python是解释型语言，你的代码在执行时会一行一行地翻译成CPU能理解的机器码，这个翻译过程非常耗时，所以很慢。而C程序是运行前直接编译成CPU能执行的机器码，所以非常快。
* 获取用户输入`str=input('请输入:')`，获取的是string类型，可以通过`int()`函数转为整型
* Python提供一个`range()`函数，可以生成一个整数序列，再通过`list()`函数可以转换为list
    `list(range(5)) = numList=[0,1,2,3,4]`
* 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
* 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
* 之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。
* 安装三方库`pip3 install Pillow`
##### 有序列表list(可变)
```python
listTest = ['A', 'B', "CCC"]
print(listTest)
# 索引从0开始
print(listTest[0])
# 直接获取倒数第一条
print(listTest[-1])
# 直接获取倒数第二条
print(listTest[-2])
# 直接获取倒数第三条
print(listTest[-3])
print(listTest[listTest.__len__() - 1])
# 获取长度
print(listTest.__len__())
print(len(listTest))

# 添加元素到队尾
listTest.append('D')
# 添加元素到指定位置
listTest.insert(0, 'AliPay')

print('添加后', listTest)
# 删除
listTest.pop()
print(listTest)
print('删除后', listTest)
listTest.pop(0)
print('删除后', listTest)

```

##### 数组tuple(元组，不可变)
```python
array = ('A', 'B', 1, 'CD')
for i in array:
    print(i)
```
##### 字典dict (map KV)
```python
map = {'腾讯': 'Tencent', '华为': 'Huawei', '小米': 'Xiaomi'}
print(map)
print(map.get('中兴'))
print(map.get('华为'))
map['腾讯'] = 'Pony'
print(map)
# 新增/修改元素
map['阿里'] = '马云'
print(map)
# 删除元素
map.pop('小米')
# 遍历dict里面的元素
for k, v in map.items():
    print(k, ':', v)
```

##### set
> 要创建一个set，需要提供一个list作为输入集合
```python
# 定义一个SET
# set1 = set([1, 1, 2, 3, 4, 6, 7, 7])
# 或者
set1 = {1, 1, 2, 3, 4, 6, 7, 7}
for item in set1:
    print(item)
print(set1)

# 添加元素
set1.add(8)
print(set1)
# 删除元素
set1.remove(8)
print(set1)

set2 = {1, 3, 11, 14, 16, 20, 20}
print('set2:', set2)
# 取交集
print('set1 & set2:', set1 & set2)
# 取并集
print('set1 | set2', set1 | set2)

```
#### 流程控制
* 条件判断 if
```python
age = 10

if age < 10:
    print('10')
elif age < 20:
    print('20')
elif age < 30:
    print('30')
else:
    print('666')

```
* 循环控制 for
```python
for i in array:
    print(i)
    
while True:
    ...
    continue;
    break;
```

### 函数
* 类型转换函数
    * int()
    * float()
    * str()
    * bool()

* 给函数取别名 `a=abs`,变量a指向abs函数
* 定义函数:定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
```python
# 定义一个函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


# 给函数取别名
yourAbs = my_abs
print(yourAbs(100))
print(yourAbs(-1100))


# 定义一个空函数
def empty():
    pass


def my_abs_2(x):
    # 类型检查
    if not isinstance(x, (int, float)):
        # 抛出异常
        raise TypeError('不支持的参数类型')
    else:
        return my_abs(x)


print(my_abs_2(10000))

# 设置参数默认值
def default(x: int, y: int = 100):
    if y == 100:
        print('马化腾')
    else:
        print('Tencent')
        
# --------------需要注意的地方
def default_parameter(x=[]):
    x.append('T')
    print(x)


default_parameter()
default_parameter()
default_parameter()

输出:
['T']
['T', 'T']
['T', 'T', 'T']

默认参数尽量是不可变参数，否则如果默认参数的值变了之后，后面这个默认参数的值就一直都是变化之后的值

# --------------

# 可变参数-可传0个或多个参数
def multi_parameter(*numbers: int):
    sum_value: int = 0
    for item in numbers:
        sum_value += item
    return sum_value


print(multi_parameter())
print(multi_parameter(1))
print(multi_parameter(11, 22, 33))
print(multi_parameter(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(multi_parameter(*range(101)))  # 传入一个tuple或者list，可以直接在前面加上*


def person(name, age, **kw):
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, city=extra['city'], job=extra['job'])
>>> person('Jack', 24, **extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}







# 默认参数
def moren(x: int, y: int = 10):
    print(x + y)

moren(5)
moren(5, 20)

# 可变参数
def kebian(x: int, *y: int):
    sum = 0
    sum += x
    for i in y:
        sum += i
    print(sum)

kebian(1)
kebian(1, 2, 3)

# 关键字参数
def guanjianzi(x: int, **y):
    print(x, y)

guanjianzi(10, a=123, b=234, c=345)
```

### 高级特性
* 切片Slice
```python
L = ['0', '1', '2', '3', '4', '5']

# 切片返回前3条（0，1，2）
print(L[:3])

# 切片返回索引为1-3但是不包含3的数据
print(L[1: 3])

# 切片返回倒数第3到倒数第1，但是不包含倒数第1个元素
print(L[-3:-1])

# 设置步长,前6个元素，每1个元素取1个
print(L[:6:1])
# 设置步长,前6个元素，每2个元素取1个
print(L[:6:2])
# 设置步长,每2个元素取1个
print(L[::2])

# 对字符串的截取(所以python没有提供substring方法)
print('ABCDEF'[:3])
```

* 迭代
```python
from collections import Iterable

myMap = {'Tencent': '小马哥', 'Alibaba': '马云', 'Baidu': '红颜祸水'}
# 遍历key
for key in myMap:
    print(key)
print('--------------')

for key in myMap.keys():
    print(key)
print('--------------')

# 遍历value
for value in myMap.values():
    print(value)
print('--------------')

# 遍历KV
for k, v in myMap.items():
    print(k, ':', v)
print('--------------')

myArray = (11, 12, 13, 14, 15)
for item in myArray:
    print(item)
print('--------------')

# 判断一个对象是否是可迭代的
print(isinstance(myArray, Iterable))
print(isinstance(myMap, Iterable))
print(isinstance('ABCDE', Iterable))
print(isinstance(123, Iterable))
print('--------------')

# 迭代时获取索引(Python内置的enumerate函数可以把一个list变成索引-元素对)
for index, item in enumerate(myArray):
    print('index=', index, ':', 'item=', item)
```

* 列表生成式
```python
import os

# 生成1到11的序列，并转成list
my_list = list(range(1, 11))
print(my_list)

# 生成复杂的数据-使用表达式
my_list_2 = list((x * x) for x in range(1, 11))
print(my_list_2)

# 打印文件与文件夹
print([item for item in os.listdir('../../../')])

# 将list中的元素转为大写形式
my_list_3 = ['Tencent', 'Alipay', 'Baidu', 'Huawei']
print('before:', my_list_3)
print('after:', [i.upper() for i in my_list_3])

```

* 生成器
```python
# 生成器：按照某种规则生成数据
# 与列表生成式的区别是，列表生成式生成的元素的确定的，有限的list。而生成器生成的元素是无限个的，是一个generator，通过next()获取下一条数据
my_generator = (x * x for x in range(1, 11))

# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))

for i in my_generator:
    print('item:', i)

# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
# 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

```

* 迭代器
```python
# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
#
# 一类是集合数据类型，如list、tuple、dict、set、str等；
#
# 一类是generator，包括生成器和带yield的generator function。
#
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
#
# 可以使用isinstance()判断一个对象是否是Iterable对象

# 凡是可作用于for循环的对象都是Iterable类型；
#
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
#
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
#
# Python的for循环本质上就是通过不断调用next()函数实现的

```

### 函数式编程
* 高阶函数
```python
print(abs(-10))

# 可以将其他字段赋值给函数名
# abs = 10
# 也可以将函数名赋值给字段
my_abs = abs
my_abs(-100)


# 编写高阶函数，就是让函数的参数能够接收别的函数。例如：abs就是一个函数
def add(x: int, y: int, abs):
    return abs(x) + abs(y)


print(add(123, 2, abs))

```

* map()与reduce()函数
```python
# map函数接收两个参数，第一个参数是一个函数f(x)，第二个参数是一个Iterator。
# map(f,Iterator)等价于遍历Iterator的每个元素，并执行f()函数。将执行的结果再组成一个list
from functools import reduce


def add_one(x: int):
    return x + 1


result = map(add_one, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# map返回的是一个Iterator，需要通过list()转为list
print(list(result))
for item in result:
    print(item)


def my_sum(x: int, y: int):
    return x + y


result2 = reduce(my_sum, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# reduce把结果继续和序列的下一个元素做累积计算，返回之后一次计算的结果
print(result2)

# 练习1
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
L1 = ['adam', 'LISA', 'barT']


# 内置函数，将首字母大写，剩下的小写
# 'AbcDE'.title()


def starUpper(x: str):
    return x[0: 1].upper() + x[1: len(x)].lower()


print(list(map(starUpper, L1)))

# 练习2
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：
L2 = [3, 5, 7, 9]
print(reduce(lambda x, y: x * y, L2))

# 练习3
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
print(float('123.456'))

```

* filter与sorted函数
```python
print(list(filter(lambda x: x > 5, [1, 3, 5, 7, 9, ])))

print(list(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=False)))

# 请用sorted()对上述列表按名字/成绩排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(list(sorted(L, key=lambda x: str(x[0]).lower())))
print(list(sorted(L, key=lambda x: x[1])))

```
### 面向对象
* 类与实例与访问限制
```python
# 定义一个class，继承自object，（所有的类都最终继承object父类）
class Student(object):
    # 构造方法
    def __init__(self, name: str, score: int):
        # public属性
        self.name = name
        # 私有属性,只能在类的内部被访问，无法从外部访问
        self.__score = score

    # 成员函数
    def print_score(self):
        print('name=', self.name, ',score=', self.__score)

    # 私有属性的getter访问器
    def get_score(self):
        return self.__score

    # 私有属性的setter
    def set_score(self, score: int):
        if score < 0:
            raise ValueError('score不能小于0')
        self.__score = score


# 在py中_x表示外部虽然可以直接访问，但是不应该直接访问的变量，这是约定

s1 = Student('futao', 100)
s1.print_score()

s2 = Student('lizi', 92)
s2.print_score()
```

* 继承与多态
```python
class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def wang(self):
        print('wang wang wang...')

    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def eat(self):
        print('eat eat eat...')

    def run(self):
        print('Cat is running...')


def run(m_object):
    m_object.run()
    pass


a1 = Animal()
a1.run()

d1 = Dog()
d1.run()
d1.wang()

d2 = Dog()
d2.run()
d2.wang()

c1 = Cat()
c1.run()
c1.eat()

c2 = Cat()
c2.run()
c2.eat()

print('-----------')
run(a1)
run(d1)
run(c1)

```

* 获取对象信息
```python
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
4面向对象

# types模块中定义了常量
print(type(123) == type('123'))

# 注意：abs属于内置函数types.BuiltinFunctionType
print(type(abs) == types.BuiltinFunctionType)
print(type(abs) == types.FunctionType)

### isinstance()函数,判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
### 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
s1 = Student('taoGe', 18)
print(s1.__dir__())


>>> hasattr(obj, 'x') # 有属性'x'吗？
True
>>> obj.x
9
>>> hasattr(obj, 'y') # 有属性'y'吗？
False
>>> setattr(obj, 'y', 19) # 设置一个属性'y'
>>> hasattr(obj, 'y') # 有属性'y'吗？
True
>>> getattr(obj, 'y') # 获取属性'y'
19
>>> obj.y # 获取属性'y'
19

如果试图获取不存在的属性，会抛出AttributeError的错误

>>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404

也可以获得对象的方法：

>>> hasattr(obj, 'power') # 有属性'power'吗？
True
>>> getattr(obj, 'power') # 获取属性'power'
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
>>> fn # fn指向obj.power
<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
>>> fn() # 调用fn()与调用obj.power()是一样的
81
```

* 实例属性与类属性
```python
# 类属性：在类定义的地方定义的属性是类属性（所有的实例对象都有类的属性）
# 实例属性：由于Python是动态语言，根据类创建的实例可以任意绑定属性。而在单独的某个实例上绑定的属性是只属于这个实例的实例属性
# 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。


class Student:
    # 类属性
    score = 100

    def __init__(self, s_name: str):
        self.s_name = s_name


s1 = Student('老司机')
# 打印出类属性
print(s1.score)
# 新增一个实例属性
s1.score = 3000
# 优先查找实例属性，所以此时输出的是3000
print(s1.score)
# 删除实例属性
del s1.score
# 查找到类属性，100
print(s1.score)

```
