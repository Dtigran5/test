def is_prime(n:int) -> bool:
    if n == 1:
        return False
    if n <= 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_list(n:int) -> list[int]:
    res = []
    for i in range(2,n):
        if is_prime(i):
            res.append(i)
    return res

print(is_prime(47))
print(prime_list(49))
