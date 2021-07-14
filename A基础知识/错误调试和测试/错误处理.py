import logging

logging.basicConfig(level=logging.INFO)

try:
    a = 0 / int(input('请输入一个数字'))
# 可同时捕获多种类型的异常
except ZeroDivisionError as ze:
    print('发生除零异常', ze)
    logging.exception(ze, '发生除零异常')
# 可同时捕获多种类型的异常
except ValueError as ve:
    print('发生整型转换异常', ve)
    logging.exception(ve, '发生整型转换异常')
# 没有发生异常
else:
    print('没有发生异常,good job')
    logging.info('没有发生异常,good job')
finally:
    print('我是必须要输出的内容')
    logging.info('我是必须要输出的内容')

# 错误类型全部继承自BaseException类
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出
# 我们从上往下可以看到整个错误的调用函数链
