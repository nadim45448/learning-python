""" explore static method and class method decorator """

class Shoping:
    def __init__(self,customer):
        self.customer=customer
        self.items=[]
        self.total=0
        pass

    def add_to_cart(self,item,price,quantity):
        
        self.items.append(item)
        item_total=price*quantity
        # self.total+=item_total
        self.add_to_total(item_total)
    
    def add_to_total(self, amount):
        self.total+=amount


    def checkout(self):
        pass
    
    @staticmethod
    def multiply(x,y):
        return x*y
    

result=Shoping.multiply(4,5)
print(result)

# result2=Shoping.add_to_total(50)

my_shoping=Shoping('rohmot ali')
my_shoping.add_to_total(100)
print(my_shoping.total)

result3=my_shoping.multiply(10,5)
print(result3)


""" we can use static method both normally and on instance """
    