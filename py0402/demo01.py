"""
生成器的使用

1、生成器的作用是节省储存空间
2、迭代到下一次的调用时，所使用的参数都是第一次所保留下的，
即是说，在整个所有函数调用的参数都是第一次所调用
时保留的，而不是新创建的
"""
import sys

# 列表生成器(循环列表)
L = [x for x in range(5)]
print(type(L))

print(sys.getsizeof(L))  # 获取列表的存储大小

# 使用生成器
g = (x for x in range(10))
print(next(g))  # 使用next获取值
print(type(g))
print(sys.getsizeof(g))

for i in g:
    print(i)
