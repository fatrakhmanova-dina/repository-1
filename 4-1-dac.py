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
        s = input('input a number from 0 to 255')
        if (s == 'q'):
            sys.exit()
        elif (s.isdigit() and int(s)%1 == 0 and 0<=int(s)<=255):
            inp = int(s)
            num = decimal2binary(inp)
            for i in range(8):
                GPIO.output(dac[i],num[i])
            print("{:.4f}".format(int(s)/256*3.3))
            time.sleep(5)
        elif not s.isdigit():
            print('please input correct number')
except ValueError:
    print('input correct number')
except KeyboardInterrupt:
    print('ended')
finally:
    GPIO.output(dac,0)
    GPIO.cleanup() 