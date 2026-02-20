from gpiozero import RGBLED
from signal import pause

rgb_led = RGBLED("GPIO13", "GPIO19", "GPIO26")

# rgb_led.color = (1, 0, 0)
# rgb_led.color = (0, 1, 0)
# rgb_led.color = (0, 0, 1)

#rgb_led.color = (0.01, 0.01, 0.01)
rgb_led.color = (0.5, 1, 0)

pause()