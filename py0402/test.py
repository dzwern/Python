# 循环遍历生成器

f = (x for x in range(10))
index = 0
while True:
    try:
        g = next(f)
        index += 1
        if index == 9:
            print(g)
    except StopIteration as e:
        print(e)
