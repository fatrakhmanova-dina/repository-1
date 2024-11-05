import bloodFunctions as b
import time
import spidev
import matplotlib.pyplot as plt

n = 20*1000


spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1600000

def getAdc():
    adcResponse = spi.xfer2([0, 0])
    return ((adcResponse[0] & 0x1F) << 8 | adcResponse[1]) >> 1

try:

    with open('/home/b03-404/results.txt', 'w') as f:

        for i in range(n+1):

            print(i)
            f.write(str(getAdc()) + ' ' + str(i/1000) + '\n')
            time.sleep(0.001)
    x = []
    y = []

    with open('/home/b03-404/results.txt', 'r') as f:
        for line in f:
            a = line.split()
            x.append(float(a[1]))
            y.append(float(a[0]))
    plt.plot(x, y)
    plt.show() 

finally:
    spi.close()  