#Read All the Sensors
import board
import time

from irsensor import IRSensors

#creating IRSensor object
ir = IRSensors(board.GP7,  board.GP5,  board.GP6,  board.GP28,
               board.GP9,  board.GP10, board.GP11, board.GP26,
               board.GP21, board.GP20, board.GP22, board.GP27)
                #sensor | en   | a    | b    | adc
                #lir    | GP7  | GP5  | GP6  | GP28
                #cir    | GP9  | GP10 | GP11 | GP26
                #rir    | GP21 | GP20 | GP22 | GP27
    
while True:
    #calls the scan method and prints all the ir values
    ir.scan()
    print(
        "lir_a:", ir.lir_a, "\t", "lir_b:", ir.lir_b, "\t",
        "cir_a:", ir.cir_a, "\t", "cir_b:", ir.cir_b, "\t",
        "rir_a:", ir.rir_a, "\t", "rir_b:", ir.rir_b)
    time.sleep(0.05)
