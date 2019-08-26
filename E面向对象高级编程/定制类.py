from typing import Any


class Chain(object):

    def __getattribute__(self, name: str) -> Any:
        if name == 'age':
            return 18
        else:
            raise AttributeError('不存在的属性', name)


c1 = Chain()
print(c1.age)
print(c1.gender)
