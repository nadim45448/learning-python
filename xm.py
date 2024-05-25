import math

class Distance:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def compute_distance(self):
        return math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)


x1, y1 = 0, 0
x2, y2 = 3, 4
distance = Distance(x1, y1, x2, y2)
print(f"The distance between the points is: {distance.compute_distance()}")  
