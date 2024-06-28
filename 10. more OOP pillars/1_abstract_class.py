from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, dim1, dim2) -> None:
        self.dim1=dim1
        self.dim2=dim2

    @abstractmethod
    def area(self):
        pass

    def show(self):
        print("nothing to show")

class Triangle(Shape):
    def area(self):
        area=0.5*self.dim1*self.dim2
        print("Area of Triangle: ", area)

obj=Triangle()


        
