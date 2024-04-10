# def square(x):
#     return x*x
# result=square(5)
# print(result)

# square=lambda x: x*x
# result=square(5)
# print(result)

# add =lambda x,y:x+y
# sum=add(4,5)
# print(sum)

numbers=[12,45,56,45,12,89]
# def double_it(x):
#     return x*2

# double_it2=lambda x: x*2

# doubled=map(double_it2, numbers)
# doubled=map(lambda x:x*2, numbers)
# print(numbers)
# print(list(doubled))

# bigger=filter(lambda x:x>50, numbers)
# print(list(bigger))

person=[
    {'name':'a','age':40},
    {'name':'b','age':25},
    {'name':'c','age':60},
    {'name':'d','age':30},
]

senior=filter(lambda x:x['age']>35, person)
print(list(senior))

junior=filter(lambda x:x['age']<35, person)
print(list(junior))





