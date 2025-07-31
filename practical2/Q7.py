#remove empty tuple from the given tuple 
a = (1, 2, (), 4, 5, ())
b = []
for i in a:
    if i != ():
        b.append(i)
b =tuple(b)
print("Tuple without empty elements:", b)
        