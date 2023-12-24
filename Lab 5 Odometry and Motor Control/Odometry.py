#Calculates the distance and the angle of the mouse
import board
import time
import rotaryio
from math import pi

lenc = rotaryio.IncrementalEncoder(board.GP12, board.GP13)
renc = rotaryio.IncrementalEncoder(board.GP19, board.GP18)

ENCODER_TICKS_PER_REVOLUTION = 206
WHEELBASE_DIAMETER = 78.0 #distance between wheels, mm
WHEEL_DIAMETER = 34.0 # mm

while True:
    wheel_circumference = pi * WHEEL_DIAMETER
    mmpertick = wheel_circumference / ENCODER_TICKS_PER_REVOLUTION
    left_dist  = lenc.position * mmpertick
    right_dist = renc.position * mmpertick

    #dist = (left_dist + right_dist) / 2
    #theta = (right_dist - left_dist) / wheelbase diameter
    dist  = (left_dist + right_dist) / 2
    theta = (left_dist - right_dist) / WHEELBASE_DIAMETER #radians
    degree = theta * pi / 180

    print(dist, theta, degree)
    time.sleep(0.05)