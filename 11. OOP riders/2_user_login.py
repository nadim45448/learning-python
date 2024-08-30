#  validate user login
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
            # return True
        else:
            print('invalid user')
            # return False
        print('password found',stored_pasword)



a=User('abul', 'nadim@gmail.com', 'abc')
a.log_in( 'nadim@gmail.com', 'abc')
