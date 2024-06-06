# base class will have only the common attributes and methods
    
class Laptop:
    def __init__(self, brand, price, color, disc_size) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.disc_size=disc_size
        pass

    def __repr__(self) -> str:
        return f'laptop: {self.brand} : {self.price} : {self.color}'
    
class Phone:
    def __init__(self, brand, price, color, camera, sim_num) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.camera = camera
        self.sim_num = sim_num
        pass

    def is_dual_sim(self):
        return self.sim_num>1
    
    def __repr__(self) -> str:
        return f'phone {self.brand} : {self.price} : {self.color}'
    
acer=Laptop('Acer', 5000, 'Black', '400 gb')
hp= Laptop('HP', 45000, 'Silver', '350 gb')

print(acer)
print(hp)

oppo = Phone('Oppo', 15000, 'black', '15mp', 2)
samsung = Phone('samSung', 21000, 'silver', '12mp', 1)
print(samsung)
print(oppo)
   