class Polynomial:
    def __init__(self, coefs):
        self.coefs = coefs


p1 = Polynomial((2, 3, 4)) # 2x^2 + 3x + 4
p2 = Polynomial((8, -1, 2)) # 8x^2 - 1x + 2

# add
p1 + p2

