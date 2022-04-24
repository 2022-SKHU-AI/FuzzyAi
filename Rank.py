from function.TrapeZoid import TrapeZoid


class Rank:
    def __init__(self):
        self.low = TrapeZoid(-100, 0, 6, 9)
        self.high = TrapeZoid(6, 8, 100, 200)

    def value(self, x):
        return self.low.value(x), self.high.value(x)