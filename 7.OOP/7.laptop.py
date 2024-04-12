"""  """
class Laptop:
    def __init__(self,brand,age):
        self.brand=brand
        self.age=age
    
    def increase_age(self,age=1):
        self.last_age=self.age
        # self.age+=1
        self.age=self.age+age

    def repair(self, life_increase=-5):
        self.increase_age(life_increase)


my_laptop=Laptop('Acer',1)
# print(my_laptop.age)
my_laptop.increase_age()
my_laptop.increase_age()
# print(my_laptop.age)
# my_laptop.age=5
# print(my_laptop.age)
# my_laptop.increase_age()
# my_laptop.increase_age()
# my_laptop.increase_age()
# print(my_laptop.age)

her_laptop=Laptop('Apple', 1)
her_laptop.increase_age()
her_laptop.increase_age()
her_laptop.increase_age()
# print(her_laptop.age)
# print(her_laptop.last_age)
her_laptop.age=18
print(her_laptop.age)
her_laptop.repair(-6)
print(her_laptop.age)
print(her_laptop.__dict__)
        