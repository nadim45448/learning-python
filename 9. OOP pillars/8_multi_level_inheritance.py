# A->B->C.....

class A:
    
    def display1(self):
        print("Inside class A")
class B(A):
    # Display1
    def display2(self):
        print("Inside class B")
class C(B):
    # Display1, Display2
    # super().display2()
    def display3(self):
        print("Inside class C")

obj1=C()
obj1.display1()
obj1.display2()
obj1.display3()
