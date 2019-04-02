"""
时间消耗装饰器
生成器+装饰器
"""

import time


# 装饰器的使用
def timecount(f):
    def tc():
        start = time.time()
        f()
        end = time.time()
        print(f.__name__, "消耗了", end - start)

    return tc


@timecount
def getfromlist():
    list1 = [x for x in range(100000)]
    print(list1.index(99999))


# 循环遍历生成器
@timecount
def getfromgeberator():
    g1 = (x for x in range(100000))
    index = 0
    while True:
        try:
            result = next(g1)
            index += 1
            if index==99999:
                return result

        except StopIteration as e:
            print(e)


getfromlist()
getfromgeberator()
