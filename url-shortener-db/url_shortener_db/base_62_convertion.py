class Base62Convertion:
    def __init__(self):
        self.BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.BASE62_len = len(self.BASE62)

    def encode(self, number):
        if number == 0:
            return self.BASE62[0]

        arr = []
        while number:
            number, rem = divmod(number, self.BASE62_len)
            arr.append(self.BASE62[rem])
        arr.reverse()
        return "".join(arr)

    def decode(self, string):
        strlen = len(string)
        num = 0

        # idx = 0
        for index, char in enumerate(string):
            power = strlen - (index + 1)
            num += self.BASE62.index(char) * (self.BASE62_len**power)
            # idx += 1

        return num


cl = Base62Convertion()
lol = cl.encode(1649885634096)
print(lol)
print(cl.decode(lol))
