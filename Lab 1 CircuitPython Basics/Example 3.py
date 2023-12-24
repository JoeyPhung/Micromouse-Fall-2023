#Example 3: Button Blinky
#Utilizes the button on the PCB to decide when the Neopixel is turned on
import board
import neopixel
import digitalio

rgb = neopixel.NeoPixel(board.GP4, 1)

but = digitalio.DigitalInOut(board.GP3)
but.pull = digitalio.Pull.UP

while True:
    if but.value: #button not pressed
        rgb[0] = (0, 0, 0)
    else: #button pressed
        rgb[0] = (0, 100, 100)