class Trti():
    def __init__(self,a, h):
        self.a = a
        self.h = h

    def dfg(self):
        return self.a * self.h *2
a = Trti(7,6)
print(a.dfg())
