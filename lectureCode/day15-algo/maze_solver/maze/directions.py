class direction(int):
    @property
    def left(self):
        n = self >> 1
        if n == 0:
            n = 8
        return direction(n)

    @property
    def right(self):
        n = self << 1
        if n == 16:
            n = 1
        return direction(n)

    @property
    def back(self):
        if self >= 4:
            return direction(self >> 2)
        else:
            return direction(self << 2)

N = direction(1)
E = direction(2)
S = direction(4)
W = direction(8)


