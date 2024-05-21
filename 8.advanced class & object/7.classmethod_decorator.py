""" explore static method and class method decorator """

""" only class er kichu jinis e access thakbe """
class Shoping:
    mall='Jamuna Furture Park'
    hours=[]
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
    @classmethod
    def opening_hour(cls,day):
        return cls.mall
    
