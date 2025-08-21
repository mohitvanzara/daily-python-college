# 4.	Write a function to return the sum of two numbers. Defined sum as global and local variable and see the difference
local_sum = 100
def sum_numbers(a, b):
    global sum
    sum = a + b  # Global variable
    local_sum = a + b  # Local variable
    return local_sum, sum

print(sum_numbers(5, 10))
print(sum)        #'sum' is global
print(local_sum)
# 'local_sum' is not defined outside the function