import matplotlib.pyplot as plt

with open('data_0.txt', 'r') as file:
    data_0_clean = [int(x.strip('\n')) for x in file.readlines()]
    data_0c_max_values = [max(data_0_clean[i - 150:i]) for i in range(150, len(data_0_clean), 150)
                          if max(data_0_clean[i - 150:i]) != 4095]
with open('data_0_co2.txt', 'r') as file:
    data_0_human = [int(x.strip('\n')) for x in file.readlines()]
    data_0h_max_values = [max(data_0_human[i - 150:i]) for i in range(150, len(data_0_human), 150)
                          if max(data_0_human[i - 150:i]) != 4095]
with open('data_1.txt', 'r') as file:
    data_1_clean = [int(x.strip('\n')) for x in file.readlines()]
    data_1c_max_values = [max(data_1_clean[i - 150:i]) for i in range(150, len(data_1_clean), 150)
                          if max(data_1_clean[i - 150:i]) != 4095]
with open('data_1_co2.txt', 'r') as file:
    data_1_human = [int(x.strip('\n')) for x in file.readlines()]
    data_1h_max_values = [max(data_1_human[i - 150:i]) for i in range(150, len(data_1_human), 150)
                          if max(data_1_human[i - 150:i]) != 4095]
print(data_0h_max_values, data_1h_max_values)
x_1 = [i / 500 for i in range(len(data_0_clean))]
y_1 = data_0_clean

x_2 = [i / 500 for i in range(len(data_1_clean))]
y_2 = data_1_clean
#t_1, t_2 = x_1[y_1.index(3367)], x_2[y_2.index(4052)]
plt.figure(dpi=100)

plt.ticklabel_format(style='sci',
                     axis='both',
                     scilimits=(0, 0),
                     useMathText=True)
plt.plot(x_1, y_1)
plt.plot(x_2, y_2)
#plt.axvline(x=t_1, linestyle='--', color='red', label='t_1')
#plt.axvline(x=t_2, linestyle='--', color='green', label='t_2')
plt.minorticks_on()

plt.grid(visible=True,
         which='major',
         linestyle='-',
         linewidth=1.5,
         color='0.7')
plt.grid(visible=True,
         which='minor',
         linestyle='-',
         linewidth=1,
         color='0.8')

plt.xlim([0, max(x_1 + x_2) * 1.05])
plt.ylim([0, max(y_1 + y_2) * 1.05])

plt.title('Зависимость давления от числа отсчётов\nЧистый воздух')
plt.xlabel(r'$t, мс$')

plt.legend(loc='upper left')
plt.show()
