#Example 2: Unnecessarily Complex Blinky
#Lights up the Neopixel red every 5th cycle (2 seconds) for half a second
import board
import time
import neopixel

rgb = neopixel.NeoPixel(board.GP4, 1)

counter = 0
while True:
    counter += 1
    if counter % 5 == 0: # modulus a.k.a remainder
        rgb[0] = (100, 0, 0)
        time.sleep(0.5)
        rgb[0] = (0, 0, 0)
    else:
        #wait 0.5 seconds
        for i in range(5): # 0, 1, 2, 3, 4
            time.sleep(0.1)