# 4.Write a Python program to get the frequency of the elements in a list.
# import time

# start_time = time.time()
#     # Your code here
# a = [1, 2, 5, 11, 11]
# b = []
# for i in range(len(a)):
#     if a[i] not in b:
#         b.append(a[i])
#         cnt = 0
#         for j in range(len(a)):
#             if a[i] == a[j]:
#                 cnt += 1
#         print(a[i], cnt)


# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Execution time: {elapsed_time:.4f} seconds")




# using dictionary to get frequency of elements in a list

import time

start_time = time.time()
a=[1,2,5,11,11]
frequency_dict ={}
for i in a:
    if i in frequency_dict:
        frequency_dict[i] += 1
    else:
        frequency_dict[i] = 1
for key, value in frequency_dict.items():
    print(f"{key}: {value}")

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.4f} seconds")








