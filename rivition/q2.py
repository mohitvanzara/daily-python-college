a=0
b=1
n = int(input())
print(a)
print(b)
i = 0
while(i<=n):
    c=a+b
    a = b
    b = c
    i=i+1
    print(c)