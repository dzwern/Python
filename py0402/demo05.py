class Good():
    def __init__(self, addr):
        self.addr = addr
        self.index = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.index < len(self.addr):
            result = self.addr[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration("越界")


g = Good(["zhengzhou", "anyang", 'nanyang'])

print(g)

a = (x for x in g)
print(a)

