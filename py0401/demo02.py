# 编写代码添加类属性，实例属性，类方法，静态方法，实例方法，
# 分析区别以及调用逻辑 删除指定 属性

import types


class Good():
    """
    这是一个商品类型
    """
    # 使用slots限制动态添加内容
    __slots__ = ("name", "price", "addr", "get")

    def __init__(self, _name):
        self.name = _name


a1 = Good("tea")
a2 = Good("coffee")


# 通过类名添加类属性 通过实例名添加实例属性
# 动态添加 实例方法 类方法 静态方法
def getname(self):
    print(self.name)


# 动态的添加实例方法
a2.get = types.MethodType(getname, a2)
a2.get()


@classmethod
def gets(cls):
    print(cls.__doc__)

#动态的添加类方法
Good.gets=gets
#类方法
Good.gets()
#实例方法
a1.gets()

@staticmethod
def get():
    print("静态方法")

Good.get=get
Good.get()

# delattr(Good,"get")
#
# if hasattr(Good, "get"):
#     print("存在get")
# else:
#     print("不存在get")


