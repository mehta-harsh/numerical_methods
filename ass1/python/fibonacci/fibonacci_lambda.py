#I've used an online website "www.tutorialspoint.com" as a reference for this code
from functools import reduce
fib_numbers = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])
print(fib_numbers(10))
