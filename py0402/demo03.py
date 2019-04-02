# 斐波那契数列

def fun(num):
    a, b = 0, 1
    yield a
    yield b

    count = 0

    while count < num:
        a, b = b, a + b
        yield b
        count += 1


# result的类型为生成器类型
# <generator object fun at 0x000001C34F716830>
result = fun(10)
print(result)

for r in result:
    print(r)
