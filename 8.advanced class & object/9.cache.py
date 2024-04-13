""" cache decorator, function tools and partial function """

#  1 1 2 3 5 8 13 21 .....

import time
from functools import cache

@cache
def fib(n):
    if n<=1:
        return 1
    return fib(n-1)+fib(n-2)

start=time.time()
for i in range(20):
    print(i,fib(i))

end=time.time()
time_taken=(end-start)*1000
print('Time taken:',time_taken)

