numbers=[12,5,8,20,50,98,11,29,61]
odd_numbers=[]
for num in numbers:
    if num%2!=0:
        odd_numbers.append(num)
# print(odd_numbers)

odd_numbers2=[num for num in numbers if num%2!=0]
# print(odd_numbers2)

names=['sakib','tamim','mushi']
ages=[37,39,36]
pairs=[(name,age) for name in names for age in ages if age<45]
print(pairs)

