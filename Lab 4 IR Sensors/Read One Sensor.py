#code to read from one sensor
import board
import time
import digitalio
from analogio import AnalogIn

l_en  = digitalio.DigitalInOut(board.GP7)  #create DigitalInOut output on GP7
l_en.direction = digitalio.Direction.OUTPUT
l_en.value = False
l_adc = AnalogIn(board.GP28) #create AnalogIn on GP28

l_a   = digitalio.DigitalInOut(board.GP5)
l_a.direction  = digitalio.Direction.OUTPUT
l_a.drive_mode = digitalio.DriveMode.OPEN_DRAIN
l_a.value = True # high Z mode

l_b = digitalio.DigitalInOut(board.GP6) #create DigitalInOut on GP6 in open-drain mode
l_b.direction  = digitalio.Direction.OUTPUT
l_b.drive_mode = digitalio.DriveMode.OPEN_DRAIN
l_b.value = True # high Z mode

while True:
    l_en.value = True #enable IR emitters using l_en

    l_a.value = False #enable chosen sensor l_a
    time.sleep(0.001) #wait a bit
    print(l_adc.value, end=" ") #take analog reading for future printing
    l_a.value = True #disable chosen sensor l_a

    l_b.value = False #enable chosen sensor l_b
    time.sleep(0.001) #wait a bit
    print(l_adc.value, end=" ") #take analog reading for future printing
    l_b.value = True #disable chosen sensor l_b

    l_en.value = False #disable IR emitters using l_en
    time.sleep(0.05)
    print()