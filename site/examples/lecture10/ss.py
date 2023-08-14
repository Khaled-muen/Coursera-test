class PLayer:
    def __init__(self, X, y):
        self.X = X
        self. y = y
        self.health = 100
    def move(self, dx, dy):
        self.X += dx
        self. y += dy
    def damage(self, pts):
        self.health -= pts
a= PLayer(2, 3)
a. damage (2)
a. move (1, 2)
print (a.X+ a.y + a.health)