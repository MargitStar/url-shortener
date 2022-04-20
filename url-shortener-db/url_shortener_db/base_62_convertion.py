class Base62Convertion:
    BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    BASE62_LEN = len(BASE62)

    def encode(self, number):
        if number == 0:
            return self.BASE62[0]

        arr = []
        while number:
            number, rem = divmod(number, self.BASE62_LEN)
            arr.append(self.BASE62[rem])
        return "".join(reversed(arr))

    def decode(self, string):
        strlen = len(string)
        num = 0

        for index, char in enumerate(string):
            power = strlen - (index + 1)
            num += self.BASE62.index(char) * (self.BASE62_LEN**power)

        return num
