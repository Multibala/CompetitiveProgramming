from functools import cached_property

@cached_property
def fib(n):
    if n<=1:
        return n
    return fib(n - 1)  + fib(n - 2)

for i in range(400):
    print(i,fib(i))
