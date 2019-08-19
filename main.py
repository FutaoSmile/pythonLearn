# 通过class定义一个类，object为需要继承的父类，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类
class Student(object):
    # 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
    # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
    #  __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # def __init__(self,name):
    #     self.name=name

    def print_info(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            print('A')
        elif self.score >= 60:
            print('B')
        else:
            print('C')


s1 = Student('futao', 98)
s1.print_info()
s1.get_grade()

s2 = Student('moxi', 66)
s2.print_info()
s2.get_grade()
