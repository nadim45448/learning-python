class Bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_withdraw=100
        self.max_withdraw=200000

    def get_balance(self):
        return self.balance
    
    def withdraw(self,amount):
        if amount<self.min_withdraw:
            return f'no money for you. Minimum withdraw:{self.min_withdraw}'
        elif amount>self.max_withdraw:
            return f'you cross max limit:{self.max_withdraw}'
        elif amount>self.balance:
            return 'insufficient money'
        else:
            self.balance-=amount
            return f'Here is your money:{amount}'

    def deposit(self,amount):
        self.balance+=amount




my_bank=Bank(80000)
reply=my_bank.withdraw(31000)
print(reply)

print("your balance:",my_bank.get_balance())
my_bank.deposit(5000)
print(my_bank.get_balance())
        

        
            
            
        
