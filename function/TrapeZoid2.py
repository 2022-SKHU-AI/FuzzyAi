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
            return x
        elif self.c<x<=self.d:
            return (self.d-x)/(self.d-self.c)
        else:
            return 0

'''
class TrapeZoid:
    def __init__(self, 15, 25, 35, 45):
        self.15 = 15
        self.b = b
        self.c = c
        self.d = d

    def value(self, x):
        if x<=self.15:
            return 0
        elif self.15<x<=self.25:
            return (x-self.15)/(self.25-self.15)
        elif self.25<x<=self.35:
            return 1
        elif self.35<x<=self.45:
            return (self.45-x)/(self.45-self.35)
        else:
            return 0
'''