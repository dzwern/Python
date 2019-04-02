"""
装饰器：为了扩展函数的功能

由闭包+语法糖
@

解释器解释道有装饰器的函数，会改变函数结构
把函数作为参数传给装饰器，并且执行装饰器的返回值（装饰器返回的为内部函数）
把装饰器内部函数付给被装饰函数
"""


def selectgoods():
    print("开始查询商品列表")


selectgoods()


# 在查询逻辑之前需要添加权限验证

def selectgoods():
    user = input("请输入用户名")
    if user == "zzy":
        print("开始查询商品")
    else:
        print("无权限")


# 调用
selectgoods()


# 使用装饰器进行操作
# 闭包+语法糖
def check(fun):
    def ck():
        user = input("输入用户名")
        if user == "zzy":
            fun()
        else:
            print("无权限")

    return ck


@check
def selectgoods():
    print("开始查询商品列表")


# 使用selectgoods函数没有变化（与上面的函数进行对比分析）
selectgoods()

"""
装饰器的执行逻辑
检测到selectgoods拥有的装饰器@check
不执行selectgoods而是将selectgoods作为参数
传入check方法，并且执行check方法，此时fun=selectgoods
将check的执行结果返回，即将ck方法引用返回
即实际执行的是ck方法。
"""


# 不加装饰器的写法
def selectgoods():
    print("开始查询商品列表")


selectgoods = check(selectgoods)
selectgoods()
