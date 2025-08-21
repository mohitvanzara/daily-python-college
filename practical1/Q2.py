# 2.	Initialize variable with strings. Take a string input from the user and output true if it exists in the array, otherwise output false.
# Initialize a list of strings
strings = ["apple", "banana", "cherry", "date", "elderberry"]
# Take input from the user
user_input = input("Enter a string to check if it exists in the list: ")
# Check if the input string exists in the list
if user_input in strings:
    print("True, the string exists in the list.")
else:
    print("False, the string does not exist in the list.")