def func(n):
    if n > 0 and ( n & (n - 1)) == 0:
        return f"{n} the number is power of 2"
    else:
       return f"{n} the number is not power of 2"

print(func(16))

