""" partial function """

from functools import partial
def get_number(a,b,c,d):
    return a*1000 +b*100+c*10+d

# number=get_number(4,5,3,2)
# print(number)

# third_only=partial(get_number,b=0,c=0, d=0)
# number2=third_only(3)
# print(number2)

num=partial(get_number,d=0,b=0,c=0)
result=num(4)
print(result)