import RPi.GPIO as GPIO
import sys
import time
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

dac = [8,11,7,1,0,5,12,6]
inp = 0
res = 0 
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
try:
    while(True):
        T = input('input a period')
        if (T == 'q'):
            sys.exit()
        elif (T.isdigit()):
            for i in range(256):
                GPIO.output(dac, decimal2binary(i))
                time.sleep(int(T)/512)
            for j in range(255, 0, -1):
                GPIO.output(dac, decimal2binary(j))
                time.sleep(int(T)/512)
        elif not T.isdigit():
            print('please input a number')
except ValueError:
    print('input correct number')
except KeyboardInterrupt:
    print('ended')
finally:
    GPIO.output(dac,0)
    GPIO.cleanup() 