print(list(filter(lambda x: x > 5, [1, 3, 5, 7, 9, ])))

print(list(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=False)))

# 请用sorted()对上述列表按名字/成绩排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(list(sorted(L, key=lambda x: str(x[0]).lower())))
print(list(sorted(L, key=lambda x: x[1])))


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, range(1, 20))))

# 匿名函数
print(list(filter(lambda n: n % 2 == 1, range(1, 20))))
