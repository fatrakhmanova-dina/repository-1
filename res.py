import matplotlib.pyplot as plt
import numpy as np

R = 8.31446
T = 298.54


def co2(v):
    m_noa, c_p_noa, c_v_noa = 0.02897, 1.0036, 0.7166
    m_w, c_p_w, c_v_w = 0.01801, 1.863, 1.403
    m_g, c_p_g, c_v_g = 0.04401, 0.838, 0.649

    x_w = 0.447 * 3170 / 101300
    x_noa_1 = 1 - x_w

    a = v ** 2 * (m_g * c_v_g - m_noa * c_v_noa) * (m_g - m_noa)
    b = R * T * (m_noa * c_p_noa - m_g * c_p_g) + v ** 2 * ((m_g * c_v_g - m_noa * c_v_noa) *
                                                            (m_noa * x_noa_1 + m_w * x_w) +
                                                            (m_noa * c_v_noa * x_noa_1 +
                                                             m_w * c_v_w * x_w) *
                                                            (m_g - m_noa))
    c = (v ** 2 * (m_noa * c_v_noa * x_noa_1 + m_w * c_v_w * x_w) * (m_noa * x_noa_1 + m_w * x_w) -
         R * T * (m_noa * c_p_noa * x_noa_1 + m_w * c_p_w * x_w))

    d = b ** 2 - 4 * a * c
    x_g = (d ** 0.5 - b) / (2 * a)
    return x_g


v_data = np.array([float(x) for x in range(3350, 3470)]) / 10
co2_data = np.array(co2(v_data))

plt.figure(dpi=100)

plt.ticklabel_format(style='sci',
                     axis='both',
                     scilimits=(0, 0),
                     useMathText=True)
plt.plot(co2_data, v_data, label='Аналитическая зависимость')
plt.plot(co2(345.26), 345.26, 'o', label=f'Значения в воздухе: 345.26 м/с, '
                                         f'{round(co2(345.26) * 100, 2)} %')
plt.plot(co2(343.01), 343.01, 'o', label=f'Значения в выдохе: 343.01 м/с, '
                                         f'{round(co2(343.01) * 100, 2)} %')
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

plt.xlim([0, np.max(co2_data) * 1.05])
plt.ylim([np.min(v_data), np.max(v_data)])

plt.title('Зависимость скорости звука\nот концентрации углекислого газа')
plt.xlabel(r'Концентрация СО2, [%]')
plt.ylabel(r'Скорость звука, [м/с]')
plt.legend(loc='upper right')

plt.show()