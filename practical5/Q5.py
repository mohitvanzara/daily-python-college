# 5.	write a python program to reverse the string using function and while loop
# def reverse_string(s):
#     reversed_str = ""
#     index = len(s) - 1
#     while index >= 0:
#         reversed_str += s[index] # concatenate character at index
#         index -= 1
#     return reversed_str

# print(reverse_string("mohit"))


a ="mohitvanzara"
b = a[0:5:-1]
print(b)  

# def reverse_words(s):
#     words = s.split()
#     return " ".join(words[::-1])

# print(reverse_words("mohit vanzara is a good"))