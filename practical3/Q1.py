# Take integer input from the user until user presses 'q' to quit.
numbers = []

while True:
    user_input = input("Enter an integer (press 'q' to quit): ")
    if user_input == 'q':
        break
    if user_input != 'q':
        num = int(user_input)
        numbers.append(num)

if numbers:
    average = sum(numbers) / len(numbers)
    product = 1
    for num in numbers:
        product *= num
    print("Average:", average)
    print("Product:", product)
else:
    print("No numbers entered.")
