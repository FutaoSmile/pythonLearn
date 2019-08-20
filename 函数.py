import math


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


def my_abs_2(x: int):
    # 类型检查
    if not isinstance(x, (int, float)):
        # 抛出异常
        raise TypeError('不支持的参数类型')
    else:
        return my_abs(x)


def hanshu(x: int, y: str):
    if x > 1:
        return x
    else:
        return y


def my(x: int, y: str):
    return x, y


print(my_abs_2(10000))


# 设置参数默认值
def default(x: int, y: int = 100):
    if y == 100:
        print('马化腾')
    else:
        print('Tencent')


def default_parameter(x='1'):
    print(x)
    x = '000'


default_parameter()
default_parameter()
default_parameter()


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
