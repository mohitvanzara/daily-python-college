# Take integer input from the user until user presses 'q' to quit.
numbers = []
while True:
    user = input("Enter an input (or 'q' to quit):")
    if user=='q':
        break
    try:
        num = int(user)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter an integer or 'q' to quit.")

if numbers :
    avg = sum(numbers)/ len(numbers)
    product =1
    for num in numbers:
        product *= num
    print(f"Average of entered numbers: {avg}") 
    print(f"Product of entered numbers: {product}")
else:
    print("No numbers were entered.")   