class Phone:
    brand='Apple'
    color='Black'
    price='100000'
    variant=''

my_phone=Phone()
# print(isinstance(my_phone,Phone))
print(my_phone.brand)
print(my_phone.color)
print(my_phone.price)
my_phone.variant="USA"
print(my_phone.variant)

your_phone=Phone()
his_phone=Phone()
her_phone=Phone()
