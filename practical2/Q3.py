# 3.	Write a Python program that takes two lists and returns True if they have at least one common element.
# Creating a list with duplicates
my_list_1 = [1, 2,4, 4,2, 3]
my_list_2 = [4,5,6,7]
empty_list =[]
bool  = False

for i in my_list_2:
    if i in my_list_1:
        empty_list.append(i)
        bool = True
        break

print(bool)
print("Common elements:", empty_list)
