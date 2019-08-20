import os

# 生成1到11的序列，并转成list
my_list = list(range(1, 11))
print(my_list)

# 生成复杂的数据-使用表达式
my_list_2 = list((x * x) for x in range(1, 11))
print(my_list_2)

print([item for item in os.listdir('../../../')])

# 将list中的元素转为大写形式
my_list_3 = ['Tencent', 'Alipay', 'Baidu', 'Huawei']
print('before:', my_list_3)
print('after:', [i.upper() for i in my_list_3])
