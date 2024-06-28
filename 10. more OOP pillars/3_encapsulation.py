# data hiding

class Account:
    def __init__(self, holder, initial_balance) -> None:
        self.holder=holder #public attribute'
        self._account_number=156 # _account_number is a protected attribute
        self.__balalnce=initial_balance # __balance is a private attribute

    def deposit(self, amount):
        print(f'adding {amount} to your acount')
        self.__balalnce+=amount

    def withdraw(self, amount):
        print(f'Withdrawing {amount} from your account')
        self.__balance -= amount

class StudentAccount(Account):
    def __init__(self, holder, initial_balance, school) -> None:
        self.school=school
        super().__init__(holder, initial_balance)
    
    def get_balance(self):
        return self._account_number
    
nadim=StudentAccount('nadim', 50000, 'AIUB')
# print(nadim.__balalnce)
print(nadim.holder)
nadim.deposit(2000)
nadim.deposit(30000)
print(nadim.get_balance())
# nadim.__balalnce=0
# nadim._account_number=125
print(nadim._account_number)
