# 사다리꼴 형태 소속함수
class TrapeZoid:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def value(self, x):
        if x<=self.a:
            return 0
        elif self.a<x<=self.b:
            return (x-self.a)/(self.b-self.a)
        elif self.b<x<=self.c:
            return 1
        elif self.c<x<=self.d:
            return (self.d-x)/(self.d-self.c)
        else:
            return 0