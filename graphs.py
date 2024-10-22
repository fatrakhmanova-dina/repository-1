import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#with open("/home/b03-404/py/data.txt", "r") as data:
#    tmp = [float(i) for i in data.read().split("\n")]
data_array = np.loadtxt("/home/b03-404/py/data.txt", dtype=float)
T = 1 / 0.04942000093798952 
#print(len(data_array))
maxdata = np.argmax(data_array)
mindata = np.argmin(data_array)
#print(maxdata)
#print(mindata)
time_array = [T * i / 100 for i in range(0, len(data_array))]
t1 = time_array[maxdata]
t2 = time_array[len(time_array) - 1] - time_array[maxdata]
fig, ax = plt.subplots()
ax.set_title('Зависимость напряжения на конденсаторе от времени')
ax.plot(time_array, data_array, label='U(t)')
ax.legend(loc='best')
plt.figtext(0.5, 0.6, "Время зарядки " + str(t1) + 'c', fontsize=8)
plt.figtext(0.5, 0.5, "Время разрядки " + str(t2) +'c', fontsize=8)
ax.set_ylabel('U(B)')
ax.set_xlabel('t(с)')
plt.grid(which='major')

plt.grid(which='minor', linestyle=':')
plt.minorticks_on()
plt.tight_layout()
fig.tight_layout()
plt.savefig("/home/b03-404/py/graph.png")
plt.show()  
