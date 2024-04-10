numbers=[12,5,8,20,50,98]
numbers_iter=iter(numbers)
try:
    print(next(numbers_iter))
    print(next(numbers_iter))
    print("exploring iterator")
    print("but confused about it")
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
except StopIteration:
    print("Iteration end")