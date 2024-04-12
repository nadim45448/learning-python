class Shopper:
    def __init__(self,name):
        self.name=name
        self.cart=[]

    def add_to_cart(self, item,price, quantity):
        self.cart.append({'name':item,'price':price, 'quantity':quantity})
        
    def checkout(self,amount):
        # print(self.cart)
        price=0

        for item in self.cart:
            print(item)
            price=price+item['price']*item['quantity']
        if amount<price:
            return f'Please pay more money:{price-amount}'
        elif amount>price:
            return f'Here are the items and extra money:{amount-price}'
        else:
            return 'Here are your item, Thank you'


shopping=Shopper('ali mia') 
shopping.add_to_cart('shirt',450,3)
shopping.add_to_cart('shoes',899,4)
shopping.add_to_cart('pant',1400,2)
reply=shopping.checkout(5000+2746)
print(reply)

