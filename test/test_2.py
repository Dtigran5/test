#s = set(1, 4, "sad", [1,2], (3,4), "b") #error: set expected at most 1 argument, got 6
#print(s)

#s1 = set((1, 4, "sad", [1,2], (3,4), "b")) #error:unhashable type: 'list' 
#print(s1)

#s2 = set(1, 4, "sad", (3,4), "b") #error: set expected at most 1 argument, got 5 (without [1,2])
#print(s2)

s3 = ((1, 4, "sad", (3,4), "b")) # it will print the set
print(s3)
