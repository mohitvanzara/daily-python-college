# importing required modules
import matplotlib.pyplot as plt
import numpy as np

# function to generate coordinates
def create_plot(ptype):
    # x-axis values from -10 to 10 with step size 0.01
    x = np.arange(-10, 10, 0.01)

    # select the type of curve
    if ptype == 'linear':
        y = x
    elif ptype == 'quadratic':
        y = x**2
    elif ptype == 'cubic':
        y = x**3
    elif ptype == 'quartic':
        y = x**4

    return x, y

# set dark background style
plt.style.use('dark_background')

# create a figure
fig = plt.figure(figsize=(10, 8))

# define subplots in a 2x2 grid
plt1 = fig.add_subplot(221)   # Top-left
plt2 = fig.add_subplot(222)   # Top-right
plt3 = fig.add_subplot(223)   # Bottom-left
plt4 = fig.add_subplot(224)   # Bottom-right

# generate data for each type
x1, y1 = create_plot('linear')
x2, y2 = create_plot('quadratic')
x3, y3 = create_plot('cubic')
x4, y4 = create_plot('quartic')

# plot each curve on its subplot
plt1.plot(x1, y1, color='cyan')
plt2.plot(x2, y2, color='yellow')
plt3.plot(x3, y3, color='lime')
plt4.plot(x4, y4, color='orange')

# add titles
plt1.set_title('Linear (y = x)')
plt2.set_title('Quadratic (y = x²)')
plt3.set_title('Cubic (y = x³)')
plt4.set_title('Quartic (y = x⁴)')

# add grid for better visibility
plt1.grid(True, linestyle='--', alpha=0.5)
plt2.grid(True, linestyle='--', alpha=0.5)
plt3.grid(True, linestyle='--', alpha=0.5)
plt4.grid(True, linestyle='--', alpha=0.5)

# adjust spacing between subplots
plt.tight_layout()

# display the figure
plt.show()
