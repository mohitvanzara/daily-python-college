# 2.	Write a function to append [11,22,33] to the existing list.
def append_to_list(lst):
    lst.append(11)
    lst.append(22)
    lst.append(33)
    return lst
list_ex = [1,2,3,4,5]
print(append_to_list(list_ex))