"""
类装饰器
"""


class Decor():
    def __init__(self, _f):
        if input("用户名") == "zzy":
            self.f = _f
            self.f()

        else:
            print("无权限")


@Decor
def fun():
    print("执行原始函数")
