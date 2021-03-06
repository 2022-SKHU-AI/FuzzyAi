import numpy as np

# 가우시안 형태 소속함수
class Gaussian:
    def __init__(self, c, sigma):
        self.c = c
        self.sigma = sigma

    def value(self, x):
        return np.exp((-(x - self.c) ** 2) / 2 * (self.sigma) ** 2)