""" explore decorator in python """

""" def timer(func):
    def inner():
        print('time strat')
        func()
        print('time end')
    return inner

@timer
def factorial():
    print('factorial of n is :')

# timer(factorial)()
factorial() """


# if function has parameter
import math
def timer(func):
    def inner(*args, **kwargs):
        print('time strat')
        func(*args, **kwargs)
        print('time end')
    return inner

@timer
def factorial(n):
    result=math.factorial(n)
    print(f'factorial of {n} is :{result}')

# timer(factorial)()
# factorial(5) ->*args
factorial(n=5) #->**kwargs
