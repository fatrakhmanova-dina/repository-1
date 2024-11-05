import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

with open('/home/b03-404/results2.txt', 'r') as f:
    for line in f:
        a = line.split()
        x.append(float(a[1]))
        y.append(float(a[0]))
a = np.polyfit(x, y, 23, rcond=None, full=False, w=None, cov=False)
gagg = np.linspace(0, max(x), 148)
plt.plot(gagg, np.polyval(gagg, a))
plt.plot(x, y)
plt.show() 

