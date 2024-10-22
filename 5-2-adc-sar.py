import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13 
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)

def adc():

    for i in range(256):
        a = 0
        b = 256
        while b - a > 1:
            c = (a + b) // 2
            GPIO.output(dac, decimal2binary(c))
            time.sleep(0.01)
            d = GPIO.input(comp)
            if d:
                b = c
            else:
                a = c + 1
    return a
p = 0
try:
    while True:
        u = adc()
        print(u, '{:.2f}v'.format(3.3*u/256))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup