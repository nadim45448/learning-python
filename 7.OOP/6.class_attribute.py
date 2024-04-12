class Shop:
    cart=[]

    def __init__(self,buyer):
        self.buyer=buyer
    
    def add_to_cart(self,item):
        self.cart.append(item)

shopper1=Shop('jodu')
shopper1.add_to_cart('Shirt')
print(shopper1.cart)

shopper2=Shop('Modu')
shopper2.add_to_cart('Lungi')
print(shopper2.cart)

""" problem of static variable
shopper2 add only lungi but cart shows shirt and lungi """

        