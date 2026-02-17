from gpiozero import TrafficLights
from time import sleep


RED = "GPIO17"
AMBER = "GPIO27"
GREEN = "GPIO22"
lights = TrafficLights(RED, AMBER, GREEN)

lights.green.on()

while True:
    sleep(4)
    lights.green.off()
    lights.amber.on()
    sleep(2)
    lights.amber.off()
    lights.red.on()
    sleep(4)
    lights.amber.on()
    sleep(2)
    lights.green.on()
    lights.amber.off()
    lights.red.off()