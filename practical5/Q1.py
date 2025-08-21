# 1.	Write a function that returns absolute value.
def absolute_value(num):
    if num <0 :
        return -num
    else:
        return num
#test the function
print(absolute_value(-5)) # output : 5
print(absolute_value(0)) # output : 0
print(absolute_value(3))  # output : 3