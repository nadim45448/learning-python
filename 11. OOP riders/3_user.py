
import hashlib

class User:
    def __init__(self, name, email, password) -> None:
        self.name=name
        self.email=email
        pwd_encrypted=hashlib.md5(password.encode()).hexdigest()
        with open('users.txt', 'w') as file:
            file.write(f'{email} {pwd_encrypted}')
        file.close()
        print(self.name, 'user created')

    @staticmethod
    def log_in(email, password):
        stored_pasword=''
        with open('users.txt','r')as file:
            lines=file.readlines()
            for line in lines:
                if email in line:
                    stored_pasword=line.split(' ')[1]
        file.close()

        hashed_password=hashlib.md5(password.encode()).hexdigest()
        if hashed_password==stored_pasword:
            print('valid user')
            return True
        else:
            print('invalid user')
            return False
        # print('password found',stored_pasword)


class Rider(User):
    def __init__(self, name, email, password, location, balance) -> None:
        self.location=location
        self.balance=balance
        super().__init__(name, email, password)
    
    def set_location(self, location):
        self.location=location

    def get_location(self):
        return self.location
    
    def request_a_trip(self):
        pass

    def start_a_trip(self, fare):
        self.balance-=fare

    
class Driver(User):
    def __init__(self, name, email, password, location, license) -> None:
        super().__init__(name, email, password)
        self.location=location
        self.license=license
        self.earning=0

    def start_a_trip(self, destination, fare):
        self.earning+=fare
        self.location=destination

a=User('abul', 'nadim@gmail.com', 'abc')
a.log_in( 'nadim@gmail.com', 'abc')
