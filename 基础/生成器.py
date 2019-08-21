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
