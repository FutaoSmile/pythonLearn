# 定义一个SET
# set1 = set([1, 1, 2, 3, 4, 6, 7, 7])
# 或者
set1 = {1, 1, 2, 3, 4, 6, 7, 7}
for item in set1:
    print(item)
print(set1)

# 添加元素
set1.add(8)
print(set1)
# 删除元素
set1.remove(8)
print(set1)

set2 = {1, 3, 11, 14, 16, 20, 20}
print('set2:', set2)
# 取交集
print('set1 & set2:', set1 & set2)
# 取并集
print('set1 | set2', set1 | set2)
