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
