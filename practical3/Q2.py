# Write a program that removes all occurrence of a given letter from string.
input_user = input("Enter a string: ")
letter = input("Enter a letter to remove: ")

result = input_user.replace(letter, "")
print("String after removing all occurrences:", result)
