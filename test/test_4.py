#with lambda function 
fib = lambda n: 1 if n <= 1 else fib(n-1) + fib(n-2)
print(fib(5))

# with recursive function
def fib(n:int) -> int:
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))

# function without recursion

def fib(n:int) -> int:
    if n <= 1:
        return 1
    else:
        f = [1,1]
        for i in range(2, n+1):
            f.append(f[-1] + f[-2])
    return f[n]

print(fib(5))
