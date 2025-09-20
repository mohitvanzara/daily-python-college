import matplotlib.pyplot as plt
import numpy as np

# Sample data: marks of students
data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5]

# Create histogram
plt.hist(data, bins=5, color='skyblue', edgecolor='black')   # 5 bins
plt.title("Histogram of Student Marks")
plt.xlabel("Marks Range")
plt.ylabel("Frequency")
plt.show()


# import matplotlib.pyplot as plt

# Sample data: sales of fruits
# fruits = ['Apple', 'Banana', 'Orange', 'Mango']
# sales = [30, 45, 10, 25]

# # Create bar plot
# plt.bar(fruits, sales, color='orange', edgecolor='black')
# plt.title("Fruit Sales")
# plt.xlabel("Fruits")
# plt.ylabel("Number of Sales")
# plt.show()
