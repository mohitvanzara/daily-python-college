# Write a python program to get Fibonacci series between 0 to 50
a=0
b=1
print(a,end=" ")
print(b,end=" ")
c = 0
while c<=50:
    c= a+b
    a = b
    b =c
    print(c,end=" ")


    