class Calculator:
    def add(self,x,y):
        return x+y
    def subtract(self,x,y):
        return x-y
    def multiply(self,x,y):
        return x*y
    def division(self,x,y):
        return x/y


cal=Calculator()
res=cal.add(2,4)
print(res)

res=cal.subtract(35,27)
print(res)
res=cal.multiply(35,27)
print(res)
res=cal.division(35,27)
print(res)