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
