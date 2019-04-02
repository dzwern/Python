# 循环遍历生成器next的方法。

f = (x for x in range(10))

while True:
    try:
        g = next(f)
        print(g)
    except StopIteration as e:
        print(e)
        break
