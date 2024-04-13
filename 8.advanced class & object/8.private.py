""" make attribute and method privatet """

class User:
    def __init__(self, name, password, phone):
        self.name=name
        self.__password=password
        self.phone=phone
        pass

    def __get_passord(self):
        print(self.__password)

    def user_login(self, name, password):
        if(name==self.name and password==self.__password):
            return True
        return False
    

steve=User('Steve Mia','abc','017111111')
# print(steve.__password)
# print(steve.phone)
# steve.__get_passord()
result=steve.user_login('Steve Mia','abc')
print(result)