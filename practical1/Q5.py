#  Write a program that adds the numbers stored in an array up to a user-defined 
# count. 

# Initialize an array of numbers
numbers = [10, 20, 30, 40, 50]
# Take input from the user for the count
count = int(input("Enter the count of numbers to sum (up to 5): "))
# Ensure the count does not exceed the length of the array
if count > len(numbers):
    count = len(numbers)
# Calculate the sum of the specified count of numbers
total_sum = sum(numbers[:count])
# Print the result
print(f"The sum of the first {count} numbers is: {total_sum}")