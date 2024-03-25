#1 (with 2 for)
ls = []
for i in range(1,7,2):
    ls1 = []
    for j in range(3):
        ls1.append(i + j)
    ls.append(ls1)
print(ls)

#2 (with comprehension)
ls = [[i + j for j in range(3)] for i in range(1,7,2)]
print(ls)

''' i = 1 j = 0,1,2 res = [1,2,3], i = 3 j = 0,1,2 res = [3,4,5], i = 5 j = 0,1,2 res = [5,6,7], the final res = [[1,2,3], [3,4,5], [5,6,7]]'''
