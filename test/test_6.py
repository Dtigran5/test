def foo(s:str) -> int:
    res = {}
    for char in s:
        if res.get(char):
            res[char] += 1
        else:
            res[char] = 1
    return res

print(foo("hello"))

# with optimizing 
def func(s:str) -> int:
    res = {}
    for char in s:
        res[char] = res.get(char, 0) + 1 #get(key, default = 0)
    return res

print(func("hello"))
