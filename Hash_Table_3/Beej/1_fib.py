# 0 1 1 2 3 5 8 13 21 34 55 O(n)
# fib(0): 0
# fib(1):1
# fib(n): fib(n-1) + fib(n-2)

cache = {}

def fib(n):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2) # O(2^n)

    return cache[n]

for i in range(100):
    print(f"{i:3} {fib(i)}")

# runtime
# everytime we make a call we are doubling the time it makes the call

# def foo (a, x, b):
#     cache[(a, x, b)] = ...

# another solution
# keep two temp lists that index previous 2 results
# does every top down solution have a bottom up solution?