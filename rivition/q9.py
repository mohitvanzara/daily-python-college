import matplotlib.pyplot as plt 
 
# defining labels 
activities = ['eat', 'sleep', 'work', 'play'] 
 
# portion covered by each label 
slices = [1, 3, 3, 3] 
 
# color for each label 
colors = ['r', 'y', 'g', 'b'] 
 
# plotting the pie chart 
plt.pie(slices, labels = activities, colors=colors, 
    startangle=90, shadow = True, explode = (0.2, 0, 0, 0), 
    radius = 1.2, autopct = '%1.1f%%') 
 
# plotting legend 
# plt.legend() 
 
# showing the plot 
plt.show() 