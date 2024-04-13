# dunder 
# majic method
# special method
""" add your own operator and majic method """
from typing import Any, SupportsIndex


class Person:
    def __init__(self,name,age, money,height=55):
        self.name=name
        self.age=age
        self.money=money
        self.height=height

    # dunder method
    def __add__(self,other):
        # return self.age+other.age
        return self.money+other.money
    
    def __call__(self):
        print(f'this is {self.name} with age {self.age} and have money {self.money}')
        pass

    def __eq__(self, other) -> bool:
        return self.age==other.age
    
    def __len__(self):
        return self.height
    def __repr__(self):
        return f'Name:{self.name}, Age:{self.age}'
        pass
    
       

alim=Person('Alim',17,500,40)
dalim=Person('Dalim',17,300)
# print(alim+dalim)

# x=3
# print(type(alim))
# alim()
# alim.__call__()

# print('compare two objects:', alim==dalim)
# print(len(alim))
print(dalim)
        
