#with recursive function
def func(n:int) -> int:
    if n < 10:
        return n
    else: 
        return n % 10 + func(n // 10)

print(func(12345))

# with lambda function
func = lambda n: n if n <10 else n % 10 + func(n // 10)
print(func(12345))

# without recursion 
def foo(n:int) -> int:
    sum_of_digit = 0
    while n > 0:
        sum_of_digit += n % 10 
        n = n // 10
    return sum_of_digit

print(foo(12345))
