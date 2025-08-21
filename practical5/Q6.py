# 6.	Write a python function that accepts a string and calculate the number of uppercase letters and lowercase letters
def count_s(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        # Using isupper() and islower() methods
        # if char.isupper():
        #     upper_count += 1
        # elif char.islower():
        #     lower_count += 1


        # Using ord() to check ASCII values
        num = ord(char)
        if 65<= num <= 90 :
            upper_count += 1

        elif 97 <= num <= 122:
            lower_count += 1

        # using range to check ASCII values
        # if 'A ' <= char <= 'Z':
        #     upper_count+=1
        # elif 'a' <= char <= 'z':
        #     lower_count+=1
    return upper_count, lower_count


print(count_s("Hello World"))