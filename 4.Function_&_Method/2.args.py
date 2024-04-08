def add(num1, num2):
    print(f'num1:{num1}, num2:{num2}')

# add(10,20)
# add(num2=20,num1=10)

def multiply(num1, num2):
    result=num1*num2
    return result
# mul =multiply(10,5)
# mul =multiply(10)
# print(mul)

def subtraction(num1, num2=15):
    result=num1-num2
    return result
sub=subtraction(35)
# print(sub)

def division(num1, num2,num5, num3=1, num4=2):
    result=num1/num2
    return result

def infinite(*numbers):
    print(numbers)

# infinite(5,7,2,3,9)


def abc(num1,num2,*numbers):
    print(num1,num2)
    print(numbers)
# abc(1,5,3,8,9)





