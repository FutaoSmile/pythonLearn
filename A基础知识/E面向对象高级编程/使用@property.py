# @property的作用是把一个方法变成属性调用
class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    # 把一个getter方法变成属性，只需要加上@property就可以了，
    # 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，
    # 于是，我们就拥有一个可控的属性操作：
    @age.setter
    def age(self, age: int):
        self.__age = age


s1 = Student('futao', 18)
print(s1.age)
s1.age = 20
print(s1.age)


# 练习
#
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
    def __init__(self, width: int, height: int, resolution: str):
        self.__width = width
        self.__height = height
        self.__resolution = resolution

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def resolution(self):
        return self.__resolution


sc1 = Screen(10, 50, 'res')
sc1.height = 100
sc1.width = 30
# sc1.resolution = '牛逼'


# 私有属性用__x标识，如果需要暴露getter方法可以在def x(self):方法上标记@property注解，
# 此时会生成@x.setter注解，可以定义在该属性的setter方法上
