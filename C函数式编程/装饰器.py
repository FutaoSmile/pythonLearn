# def log(func):
#     result = func()
#     print('----result=', result)
#     print('----functionName=', func.__name__)
#     return func


# 定义一个装饰器,这个装饰器接收一个参数，这个参数是个方法
def log(function):
    # 定义一个返回函数
    def wrapper(*p, **kv):
        # 做一些增强
        print('----', p, kv)
        # 在这个返回函数中执行原函数
        return function(*p, *kv)

    # 返回这个返回函数
    return wrapper


def log2(*text):
    print('===', text)

    def log(function):
        # 定义一个返回函数
        def wrapper(*p, **kv):
            # 做一些增强
            print('----', p, kv)
            # 在这个返回函数中执行原函数
            return function(*p, *kv)

        # 返回这个返回函数
        return wrapper

    return log


# 把@log放到now()函数的定义处，相当于执行了语句：
#
# now = log(now)
@log2('assd', '12312', '1231231')
@log
def now():
    print('2019-10-01')


now()
