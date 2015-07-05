class Point:

    def __init__(self, xcoord, ycoord):
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        self.x = xcoord
        
    def sety(self, ycoord):
        self.y = ycoord

    def get(self):
        return (self.x, self.y)
    
    def getx(self):
        return self.x
    
    def gety(self):
        return self.y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

def distance(a, b):
    xdifference = a.getx() - b.getx()
    ydifference = a.gety() - b.gety()
    return (xdifference**2 + ydifference**2)**0.5
