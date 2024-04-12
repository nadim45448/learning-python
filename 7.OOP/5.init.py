class Phone:
    manufcatured='USA' # class attribute/ static
    def __init__(self,brand,color,price):
        self.brand=brand
        self.color=color
        self.price=price

my_phone=Phone('Pixel', 'White', '85000')
# print(my_phone.price,my_phone.manufcatured)

her_phone=Phone('Apple', "Purple", '100000')
dad_phone=Phone('Huawei', 'Gray', 750000)
print(my_phone.price, her_phone.price, dad_phone.price)

print(my_phone.manufcatured, her_phone.manufcatured, dad_phone.manufcatured)

