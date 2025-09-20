#common item from two lists
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

A =set(a)
B = set(b)
common_item  = a.intersection(b)
# common_item = A & B
print("Common items:", common_item)
