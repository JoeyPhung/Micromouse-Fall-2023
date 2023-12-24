#Example 1: Blinky
#Switches the Neopixel on and off every half a second
import board     # pin definitions
import time      # time delay
import neopixel  # to control the WS2812B
import digitalio # to control the LED

print("Hello World!")

# setup the LED as an output
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# setup the WS2812B
rgb = neopixel.NeoPixel(board.GP4, 1)

# blink
while True:
    rgb[0] = (255, 255, 255) # max brightness
    led.value = True
    time.sleep(0.5)
    rgb[0] = (0, 0, 0)
    led.value = False
    time.sleep(0.5)