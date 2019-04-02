from collections.abc import Iterator, Iterable

# Iterator 迭代器 可以使用next方法
# Iterable 可迭代：可以使用for循环遍历
"""
可以直接作用于for循环的数据类型有以下几种
一类是集合数据类型：如list、tuple、dict、set、str
一类是generator 
"""

# 生成器即是可迭代，又是迭代器

# 判断是否是迭代器
# 可以使用isinstance()判断一个对象是否是Iterable对象
print(isinstance([], Iterator))  # False
print(isinstance((), Iterator))  # False
print(isinstance({}, Iterator))  # False
print(isinstance("abc", Iterator))  # False
print(isinstance(100, Iterator))  # # False
print(isinstance((x for x in range(10)), Iterator))  # True
# 判断是否可迭代

print(isinstance([], Iterable))  # True
print(isinstance((), Iterable))  # True
print(isinstance({}, Iterable))  # True
print(isinstance("abc", Iterable))  # True
print(isinstance(100, Iterable))  # False
print(isinstance((x for x in range(10)), Iterable))  # True


# 使用iter()函数进行转化
print(isinstance(iter([]),Iterator))
print(isinstance(iter("abc"),Iterator))