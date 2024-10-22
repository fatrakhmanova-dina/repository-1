import RPi.GPIO as GPIO
import time

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

leds=[2,3,4,17,27,22,10,9]
dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13 
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds,GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)

def adc():

    for i in range(256):
        a = decimal2binary(i)
        GPIO.output(dac, a)
        time.sleep(0.01)
        compval = GPIO.input(comp)
        
        if compval == 1:
            return i
    return i
p = 0
try:
    while True:
        #p = p + 1
        u = adc()
        fleds = decimal2binary(u)
        #if p % 2 != 1:
        flag = 0
        for i in range (len(fleds)):
            if fleds[i] == 1:
                flag = 1
            GPIO.output(leds[i], flag)
        print(u, '{:.2f}v'.format(3.3*u/256))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup
