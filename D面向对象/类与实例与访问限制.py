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
