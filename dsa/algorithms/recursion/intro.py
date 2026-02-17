# calling function itself untill we hit the base case
def fib(n):
    if n == 1 or n == 2: # so for the fibonacci number this is our base case when n == 1 we want to return 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2) # next fibonacci number is the sum of two previous number 

# sum to n
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
    

print(fib(10))
print(sum(4))