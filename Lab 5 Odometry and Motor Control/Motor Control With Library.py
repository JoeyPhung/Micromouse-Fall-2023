import board
import time
import pwmio
import adafruit_motor.motor as motor

#don't forget to make PWMOut objects first
lmot_in1 = pwmio.PWMOut(board.GP16, frequency=20000)
lmot_in2 = pwmio.PWMOut(board.GP17, frequency=20000)
rmot_in1 = pwmio.PWMOut(board.GP15, frequency=20000)
rmot_in2 = pwmio.PWMOut(board.GP14, frequency=20000)
#create DCMotor object on pins GP16 and GP17
lmot = motor.DCMotor(lmot_in1, lmot_in2)
#create DCMotor object on pins GP15 and GP14
rmot = motor.DCMotor(rmot_in1, rmot_in2)

#set lmot and rmot to SLOW_DECAY
lmot.decay_mode = motor.SLOW_DECAY
rmot.decay_mode = motor.SLOW_DECAY

while True:
    #move full speed forward for 1s
    lmot.throttle = 1
    rmot.throttle = 1
    time.sleep(1)
    #brake for 1s
    lmot.throttle = 0
    rmot.throttle = 0
    time.sleep(1)
    #move 25% speed backward for 1s
    lmot.throttle = -0.25
    rmot.throttle = -0.25
    time.sleep(1)
    #brake for 1s
    lmot.throttle = 0
    rmot.throttle = 0
    time.sleep(1)