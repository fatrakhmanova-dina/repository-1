import jetFunctions as j
import time


try:
    numberofmesures = 900
    j.initSpiAdc()
    j.initStepMotorGpio()
    j.stepBackward(int(numberofmesures/2))
    with open('/home/b03-404/Desktop/Фатрахманова-Шишкин-Немальцев/res09.txt', 'w') as f:
        for i in range(numberofmesures):
            time.sleep(0.01)
            f.write(str(j.getAdc()) + ' ' + str(i - numberofmesures / 2) + '\n')
            #f.write(str(j.getAdc()) + '\n')
            print(j.getAdc())
            j.stepForward(1)

finally:
    j.stepBackward(int(numberofmesures/2))
    j.deinitSpiAdc()
    j.deinitStepMotorGpio()