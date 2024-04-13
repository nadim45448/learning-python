""" use function as a parameter and return the function """

def do_something(work):
    print('start the work')
    work()
    print('done the work')
def practice_coding():
    print('I am practicing Python')

do_something(practice_coding)


""" inner function """
def outer():
    print('inside the outer function')

    def inner():
        print('inside the inner function')
    inner()
outer()


""" return inner function from outer function """

def first_function():
    print('Inside the first function')

    def second_function():
        print('Inside the second function')
    return second_function
    
first=first_function()
# print(first)
first()
first_function()()
