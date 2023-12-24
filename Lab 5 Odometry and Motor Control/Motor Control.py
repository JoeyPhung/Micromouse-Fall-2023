#Changing duty cycle values to affect wheel speed
import board
import pwmio

#create PWMOut object on pin GP16 at 20kHz
lmot_in1 = pwmio.PWMOut(board.GP16, frequency=20000)
#create PWMOut object on pin GP17 at 20kHz
lmot_in2 = pwmio.PWMOut(board.GP17, frequency=20000)

NUM_CYCLES = 65536
percentage = 0.99
do_working = False

def working():
    #set to 25% speed forward
    lmot_in1.duty_cycle = 49152
    #set to 25% speed forward
    lmot_in2.duty_cycle = 16384

def experimental():
    #need to convert float values to int
    lmot_in1.duty_cycle = int(percentage * NUM_CYCLES)
    lmot_in2.duty_cycle = int((1 - percentage) * NUM_CYCLES)

while True:
    if do_working:
        working()
    else:
        experimental()            
