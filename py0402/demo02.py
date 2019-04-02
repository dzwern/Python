# 生成器的使用
"""
函数式生成器
通过函数+yield

yield可以保存当前状态并继续执行
每一次yield向当前生成器插入对象

函数返回值变成生成器
可以使用异常捕获获得

"""


def fun():
    yield 1
    yield 2

    return "hello"


print(type(fun()))  # 查看fun的类型
print(next(fun()))  # 获取fun中的值

for i in fun():  # 通过循环获取值
    print(i)

# 通过异常捕获获取return中的值
g = fun()  # 实例化
try:
    print(next(g))
    print(next(g))
    print(next(g))  # 超过一定范围出现异常，进行捕获return值
except StopIteration as e:
    print(e, "++")
