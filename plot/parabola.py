import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 100)
plt.plot(t, t**2, color='blue', linewidth=2)
plt.title("Plot of y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
