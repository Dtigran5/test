def func(file,a,b):
    with open(file, 'r') as t:
        with open('text2.txt', 'w') as t2:
            replaced = ''
            for char in t.read():
                if char == a:
                    replaced += b
                else:
                    replaced += char
            t2.write(replaced)
    return 'text2.txt'

file ='text.txt'
a = 'a'
b = 'b'
print(func(file,a,b))

                    

