class A:
    def display(self):
        print("Inside class A")
class B(A):
    def display2(self):
        print("inside class B")

obj=B()
obj.display2()