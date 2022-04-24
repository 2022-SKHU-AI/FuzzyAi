from function.TrapeZoid import TrapeZoid


class Age:
    def __init__(self):
        self.young = TrapeZoid(-100, 0, 20, 40)
        self.old = TrapeZoid(30, 50, 200, 400)

    def value(self, x):
        return self.young.value(x), self.old.value(x)