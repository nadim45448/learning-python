# base class will have only the common attributes and methods
#  Device class is the base class
class Device:
    def __init__(self, brand, price, color) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        pass
    
    def re_sale(self):
        print('ready to sale agin')
        pass
    
class Laptop(Device): # Device class inherited by Laptop class
    def __init__(self) -> None:
        super().__init__('HP', 5000, 'Black') #to use the base classes object

        pass
    
class Phone(Device):
    def __init__(self, brand, price, color, camera, sim_num) -> None:
        super().__init__(brand, price, color) #to use the base classes object
        self.camera = camera
        self.sim_num = sim_num
        pass

    def is_dual_sim(self):
        return self.sim_num>1
    
    def __repr__(self) -> str:
        return f'phone {self.brand} : {self.price} : {self.color}'

hp=Laptop()
hp.re_sale()


print(hp.brand)


   