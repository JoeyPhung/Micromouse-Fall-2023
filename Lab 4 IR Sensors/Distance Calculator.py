#Code to detect Distances

#distance = a * sensor + b
import board
import time
from DistanceClass import Distance
from irsensor import IRSensors

#creating IRSensor object
ir = IRSensors(board.GP7,  board.GP5,  board.GP6,  board.GP28,
               board.GP9,  board.GP10, board.GP11, board.GP26,
               board.GP21, board.GP20, board.GP22, board.GP27)
                # sensor | en   | a    | b    | adc
                # lir    | GP7  | GP5  | GP6  | GP28
                # cir    | GP9  | GP10 | GP11 | GP26
                # rir    | GP21 | GP20 | GP22 | GP27

#values calculated in the calibration
dist = Distance (-0.000204865, 39.9765,  0.00351262, -117.474,
                  0.00105039,  7.79117,  0.00114322, 8.13023,
                 -0.00736501,  287.849, -0.0127969,  524.839)
                # l_a_a, l_a_b, l_b_a, l_b_b,
                # c_a_a, c_a_b, c_b_a, c_b_b,
                # r_a_a, r_a_b, r_b_a, r_b_b

while True:
    #calculates the distances for each IR sensor and prints them
    dist.calcdist(ir)
    time.sleep(0.05)
