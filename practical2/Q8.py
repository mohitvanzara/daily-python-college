#determine the list contain specific sublist
# input_sublist =list(map(int, input("Enter the sublist elements separated by space: ").split()) )
# list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]    
# for a in range(len(list_a) - len(input_sublist) + 1):
#     if list_a[a:a + len(input_sublist)] == input_sublist:
#         print(f"The sublist {input_sublist} is present in the list {list_a}.")
#         break

# print("the sublist is not present in the list")


# determine the list contain specific sublist
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# k=3
# sublists = []
# for i in range(len(list)-k+1):
#     sublists.append(list[i:i+k])
# print("All possible sublists of length", k, "are:", sublists)


# Check if a list contains a specific sublist as a sequence

main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sub_list = list(map(int, input("Enter the sublist elements separated by space: ").split()))

flag = False
for i in range(len(main_list) - len(sub_list) + 1):
    if main_list[i:i+len(sub_list)] == sub_list:
        flag = True
        break

if flag:
    print(f"The sublist {sub_list} is present in the list {main_list}.")
else:
    print(f"The sublist {sub_list} is NOT present in the list {main_list}.")


