import math
import board
import time
from math import pi
from DistanceClass import Distance
from irsensor import IRSensors
import digitalio
import neopixel
import rotaryio
import pwmio
import adafruit_motor.motor as motor

""" Constants """

ENCODER_TICKS_PER_REVOLUTION = 206
WHEELBASE_DIAMETER = 78.0 # mm
WHEEL_DIAMETER = 34.0 # mm

""" Peripherals """

# debug
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

but = digitalio.DigitalInOut(board.GP3)
but.pull = digitalio.Pull.UP

rgb = neopixel.NeoPixel(board.GP4, 1)

# encoders
lenc = rotaryio.IncrementalEncoder(board.GP12, board.GP13)
renc = rotaryio.IncrementalEncoder(board.GP19, board.GP18)

# motors
lmot = motor.DCMotor(
    pwmio.PWMOut(board.GP16, frequency=20000),
    pwmio.PWMOut(board.GP17, frequency=20000)
)
rmot = motor.DCMotor(
    pwmio.PWMOut(board.GP15, frequency=20000),
    pwmio.PWMOut(board.GP14, frequency=20000)
)
lmot.decay_mode = motor.SLOW_DECAY
rmot.decay_mode = motor.SLOW_DECAY

ir = IRSensors(board.GP7,  board.GP5,  board.GP6,  board.GP28,
               board.GP9,  board.GP10, board.GP11, board.GP26,
               board.GP21, board.GP20, board.GP22, board.GP27)
                # sensor | en   | a    | b    | adc
                # lir    | GP7  | GP5  | GP6  | GP28
                # cir    | GP9  | GP10 | GP11 | GP26
                # rir    | GP21 | GP20 | GP22 | GP27S

dist = Distance (-0.000204865, 39.9765,  0.00351262, -117.474,  # l_a_a, l_a_b, l_b_a, l_b_b,
                  0.00105039,  7.79117,  0.00114322, 8.13023,   # c_a_a, c_a_b, c_b_a, c_b_b,
                 -0.00736501,  287.849, -0.0127969,  524.839)   # r_a_a, r_a_b, r_b_a, r_b_b

""" Main """

accumulated_angle_error, prev_angle_error, accumulated_linear_error, prev_linear_error = 0, 0, 0, 0

def constrain(val, min_val, max_val):
    return min(max_val, max(val, min_val))

# compute dist and theta
def compute_odometry():
    wheel_circumference = pi * WHEEL_DIAMETER
    mmpertick = wheel_circumference / ENCODER_TICKS_PER_REVOLUTION
    left_dist  = lenc.position * mmpertick
    right_dist = renc.position * mmpertick

    dist  = (left_dist + right_dist) / 2
    theta = (left_dist - right_dist) / WHEELBASE_DIAMETER #in 
    return dist, theta

# compute correction and error terms for a target theta
def compute_u_ang(theta, theta_target):
    global accumulated_angle_error, prev_angle_error
    K_P, K_I, K_D = 0.01, 0.001, 0.01  #K_I and K_D usually 10 times smaller than

    angle_error = theta_target - theta       

    accumulated_angle_error += angle_error

    derivative_angle_error = angle_error - prev_angle_error
    prev_angle_error = angle_error

    angle_action = K_P * angle_error + K_I * accumulated_angle_error + K_D * derivative_angle_error
    return angle_action, angle_error

# compute correction and error terms for a target distance
def compute_u_lin(dist, dist_target):
    global accumulated_linear_error, prev_linear_error
    K_P, K_I, K_D = 0.01, 0.0001, 0.005 #K_I and K_D usually 10 times smaller than

    linear_error = dist_target - dist

    accumulated_linear_error += linear_error

    derivative_linear_error = linear_error - prev_linear_error
    prev_linear_error = linear_error

    linear_action = K_P * linear_error + K_I * accumulated_linear_error + K_D * derivative_linear_error
    return linear_action, linear_error

def reset_odometry():
    lenc.position, renc.position = 0, 0

def run_control_loop(theta_target, dist_target):
    dist, theta = compute_odometry()
    u_ang, e_ang = compute_u_ang(theta, theta_target)
    u_lin, e_lin = compute_u_lin(dist, dist_target)
    lmot.throttle = constrain(u_lin + u_ang, -1, 1)
    rmot.throttle = constrain(u_lin - u_ang, -1, 1)
    return e_ang, e_lin

def compute_distwall(): #TBD
    #left, center, right
    dist_between_sensors = ___
    dist = (la + lb) / 2
    theta = math.atan(dist_between_sensors / (la - lb)) #in radians 
    la, lb, ca, cb, ra, rb = dist.getdist(ir)

def forward(): #TBD
    dist, ___ = compute_odometry()
    theta = __
    #utilize IR sensors
    #drive 180 mm forward and stop,
    #maintain45 mm distance from a wall to the left
    #maintain 0 angle
    #determine the angle with respect to the wall using the two sensors

def turn_left(): #TBD
    while e_ang > ___:
        e_ang, e_lin = run_control_loop(-90,0)
    reset_odometry()

def turn_right(): #TBD
    while e_ang > ___:
        e_ang, e_lin = run_control_loop(90,0)
    reset_odometry()

def turn_around(): #TBD
    while e_ang > ___:
        e_ang, e_lin = run_control_loop(180,0)
    reset_odometry()

if __name__ == "__main__":
    goal_angle = 0 
    goal_dist = 800

    while True:
        e_ang, e_lin = run_control_loop(goal_angle, goal_dist)
        print(e_ang, e_lin, accumulated_angle_error, accumulated_linear_error)
        time.sleep(0.02) 
        if abs(e_ang) < 0.1 and abs(e_lin) < 1:
           break

    print(e_ang, e_lin, accumulated_angle_error)
    print("finished")
