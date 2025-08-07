# Write a program that removes all occurrence of a given letter from string.
input_user = input("Enter a string: ")
letter = input("Enter a letter to remove: ")
new = input("Enter a new letter to replace with: ")

result = input_user.replace(letter, new)
print(result)
