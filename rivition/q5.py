import matplotlib.pyplot as plt 
 
# x axis values 
x = [1,2,3,4,5,6,9] 
# corresponding y axis values 
y = [2,4,1,5,2,6,9] 
 
# plotting the points 
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
         marker='*', markerfacecolor='blue', markersize=12) 
 
# setting x and y axis range 
plt.ylim(0,10) 
plt.xlim(0,100) 
 
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
 
# giving a title to my graph 
plt.title('Custom plot!') 
 
# function to show the plot 
plt.show() 