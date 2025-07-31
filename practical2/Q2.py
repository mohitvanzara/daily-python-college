# 2.	Write a Python program to remove duplicates from a list
# Creating a list with duplicates
my_list = [1, 2, 2, 3, 4 ]
# Removing duplicates by converting to a set and back to a list
my_list_no_dup = list(set(my_list))
print("list without duplicates :",my_list_no_dup)