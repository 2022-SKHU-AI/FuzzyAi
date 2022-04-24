from function.Gaussian import Gaussian

# 감정 소속함수
class Feeling:
    def __init__(self):
        self.passive = Gaussian(-1, 3.3)
        self.normal = Gaussian(0, 5.2)
        self.positive = Gaussian(1, 3.3)

    def value(self, x):
        return self.passive.value(x), self.normal.value(x), self.positive.value(x)