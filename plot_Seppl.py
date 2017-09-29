import numpy as np
import matplotlib.pyplot as plt

x=np.random.normal(0,4,100000)
y=np.random.normal(0,4,100000)

plt.hist2d(x,y,bins=200)
plt.savefig('plot.pdf')
