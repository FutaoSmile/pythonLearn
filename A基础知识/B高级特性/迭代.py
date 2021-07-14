from collections import Iterable

myMap = {'Tencent': '小马哥', 'Alibaba': '马云', 'Baidu': '红颜祸水'}
# 遍历key
for key in myMap:
    print(key)
print('--------------')

for key in myMap.keys():
    print(key)
print('--------------')

# 遍历value
for value in myMap.values():
    print(value)
print('--------------')

# 遍历KV
for k, v in myMap.items():
    print(k, ':', v)
print('--------------')

myArray = (11, 12, 13, 14, 15)
for item in myArray:
    print(item)
print('--------------')

# 判断一个对象是否是可迭代的
print(isinstance(myArray, Iterable))
print(isinstance(myMap, Iterable))
print(isinstance('ABCDE', Iterable))
print(isinstance(123, Iterable))
print('--------------')

# 迭代时获取索引(Python内置的enumerate函数可以把一个list变成索引-元素对)
for index, item in enumerate(myArray):
    print('index=', index, ':', 'item=', item)


