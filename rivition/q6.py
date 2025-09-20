import matplotlib.pyplot as plt 
 
# x-coordinates of left sides of bars 
left = [1, 2, 3, 4, 5] 
 
# heights of bars 
sell_quan = [10, 24, 36, 40, 5] 
 
# labels for bars 
tick_label = ['jan', 'feb','march', 'apr', 'may'] 
 
# plotting a bar chart 
plt.bar(left, sell_quan, tick_label = tick_label, 
    width = 0.8, color = ['red', 'green','blue']) 
 
# naming the x-axis 
plt.xlabel('x - axis') 
# naming the y-axis 
plt.ylabel('y - axis') 
# plot title 
plt.title('My bar chart!') 
 
# function to show the plot 
plt.show()