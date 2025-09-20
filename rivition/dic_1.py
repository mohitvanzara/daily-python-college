A = dict({1:23,"mohit":7386})
for key,val in A.items():
    print(f"{key} and {val}")

print(A.values())

val = A.pop(6,3)
print(val)
t1 = list(A.items())
print(t1)