from typing import Any


class Chain(object):

    def __getattribute__(self, name: str) -> Any:
        if name == 'age':
            return 18
        else:
            raise AttributeError('不存在的属性', name)

    def __call__(self, *args, **kwargs):
        print('you call me ', self.age)


c1 = Chain()
print(c1.age)
# print(c1.gender)
c1()
