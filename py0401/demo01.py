'''
类与实例
类：模板定义属性和方法的封装
实例：具体的类对象，类的表现

1、实例属性会根据实例不同而不同，类属性由类决定
2、实例通常在构造赋值
3、类属性（类变量）属于类，实例属性属于实例
'''

"""
实例方法：需要第一个参数为self
类方法：需要第一个参数为cls,并且使用@classmethod声明
静态方法:需要使用@staticmethod声明

类可以调用，类方法， 静态方法
实例可以调用, 类方法，静态方法，实例方法

"""


class Good():
    """这是一个商品类"""

    def __init__(self, name):
        self.name = name

    # 这是一个实例方法
    def getname(self):
        return self.name

    # 类方法
    @classmethod
    def getinto(cls):
        print(cls.__doc__)

    # 静态方法
    @staticmethod
    def dead():
        print("静态方法")


# 只可以调用，不可以更改属性内容
# 实例属性都可以调用

a1 = Good("tea")

print(a1.getname())
a1.getinto()
a1.dead()

# 类方法
# 类属性可以调用类方法和静态方法，不能调用实例方法
# print(Good.getname()
Good.getinto()
Good.dead()
