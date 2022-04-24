from function.TrapeZoid import TrapeZoid


class Az:
    def __init__(self):
        self.veryLow = TrapeZoid(-100, 0, 15, 25)
        self.low = TrapeZoid(15, 25, 35, 45)
        self.middle = TrapeZoid(35, 45, 55, 65)
        self.high = TrapeZoid(55, 65, 75, 85)
        self.veryHigh = TrapeZoid(75, 85, 200, 400)

    def setVL(self, a, b, c, d):
        self.veryLow = TrapeZoid(-100, 0, c, d)
    def setL(self, a, b, c, d):
        self.low = TrapeZoid(a, b, c, d)
    def setM(self, a, b, c, d):
        self.middle = TrapeZoid(a, b, c, d)
    def setH(self, a, b, c, d):
        self.high = TrapeZoid(a, b, c, d)
    def setVH(self, a, b, c, d):
        self.veryHigh = TrapeZoid(a, b, 200, 400)

    def value(self, x):
        return self.veryLow.value(x), self.low.value(x), self.middle.value(x), self.high.value(x), self.veryHigh.value(x)