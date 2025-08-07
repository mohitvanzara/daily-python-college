# Write a python program that accepts a string and calculates the number of digits 
# and letters
input_str = input("Enter a string: ")
letters = sum(c.isalpha() for c in input_str)
digits = sum(c.isdigit() for c in input_str)
print("Letters:", letters)
print("Digits:", digits)