""" getter setter using property decorator """

class User:
    def __init__(self, f_name,l_name):
        self.first=f_name
        self.last=l_name
        self.email=f'{self.first}.{self.last}@user.com'
        # self.full_name=self.first+self.last

    @property #for get operation
    def full_name(self):
        return f'{self.first} {self.last}'
        # return self.full_name

    @property
    def get_email(self):
        return self.email
    
    @full_name.setter
    def full_name(self, value):
        # self.first=value.split(' ')[0]
        # self.last=value.split(' ')[1]
        first,second=value.split(' ')
        self.first=first
        self.last=second
        self.email=f'{self.first}.{self.last}@user.com'
        pass
    
    @full_name.deleter
    def full_name(self):
        del self.first
        del self.last
    
    


user=User('mark', 'zuku')

print(user.first)
print(user.last)
print(user.email)
# print(user.full_name())
print(user.get_email) #use method as attribute by property decorator
print(user.full_name)

user.full_name="robert bruce"
# del user.full_name
print(user.first)
print(user.last)
print(user.full_name)
print(user.get_email)
        