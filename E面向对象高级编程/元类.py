from D面向对象.实例属性与类属性 import Student


class Hello(object):
    def hello(self, name='world'):
        print('hello i am ', name)


h1 = Hello()
h1.hello()
print(type(h1))
# <class '__main__.Hello'>  实例的类型是class，在这里也就是Hello这个类
print(type(Hello))


# <class 'type'>            class的类型是type


# 可以通过type()函数来创建类
# 先定义函数
def fw(self, name='world'):
    print('Hello ', name)


World = type('World', (object,), dict(w_fw=fw))
# 要创建一个class对象，type()函数依次传入3个参数：
#
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 参数三：该字典对象为该类绑定的类变量和方法。其中字典的 key 就是类变量或方法名，如果字典的 value 是普通值，那就代表类变量；如果字典的 value 是函数，则代表方法。class的方法名称与函数绑定，这里我们把函数fw绑定到方法名w_fw上。
w1 = World()
w1.w_fw('123')

# todo metaclass元类
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072


