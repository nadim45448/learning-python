numbers=[12,5,8,20,50,98]

def get_numbers(nums):
    for num in nums:
        # return nums
        yield num


result=get_numbers(numbers)

print(next(result))
print(next(result))
print(next(result))
print('exploring generator')
print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))




