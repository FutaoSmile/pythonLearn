from enum import Enum, unique


@unique  # 装饰器可以帮助我们检查保证没有重复值
class UserStatus(Enum):  # 继承自枚举类Enum
    def __init__(self, status: int, description: str):
        self.__status = status
        self.__description = description

    @property
    def status(self):
        return self.__status

    @property
    def description(self):
        return self.__description

    # 定义枚举属性
    Normal = (0, '正常')
    Stop = (-1, '停用')


print(UserStatus.Normal.status)
print(UserStatus.Normal.description)
print(UserStatus.Stop.status)
print(UserStatus.Stop.description)
print(UserStatus.Stop.value)
