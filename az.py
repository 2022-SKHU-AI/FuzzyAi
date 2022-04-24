from function.TrapeZoid import TrapeZoid

# 후건부 아재개그 정도 소속함수
class Az:
    def __init__(self):
        self.veryLow = TrapeZoid(-100, 0, 15, 25)
        self.low = TrapeZoid(15, 25, 35, 45)
        self.middle = TrapeZoid(35, 45, 55, 65)
        self.high = TrapeZoid(55, 65, 75, 85)
        self.veryHigh = TrapeZoid(75, 85, 200, 400)

    def value(self, x):
        return self.veryLow.value(x), self.low.value(x), self.middle.value(x), self.high.value(x), self.veryHigh.value(x)