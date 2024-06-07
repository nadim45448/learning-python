
# example of method override
class Shape:
    def __init__(self, dim1, dim2) -> None:
        self.dim1=dim1
        self.dim2=dim2
        pass

    def area(self):
        print("I am area method of shape class")

class Triangle(Shape):
    # init, area
    def area(self): #override
        area=0.5*self.dim1*self.dim2
        print(f'area of triangle:{area}')

class Rectangle(Shape):
    # init, area
    def area(self):# override
        area=self.dim1*self.dim2
        print(f'area of triangle:{area}')

t=Triangle(10,20)
t.area()
print()

r=Rectangle(15,10)
r.area()

