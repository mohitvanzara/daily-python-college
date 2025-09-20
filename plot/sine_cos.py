import pylab as lab
import numpy as np
x = np.arange(0,5,0.1)
lab.plot(x,np.sin(2*np.pi*x))
lab.show()