# 1.	Input number through the user and find out whether the number is zero, positive or negative. 
# Take input from the user
num = float(input("Enter a number: "))
# Check if the number is zero, positive, or negative
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")