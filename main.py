# This example requires the micropython_dotstar library
# https://github.com/mattytrentini/micropython-dotstar

from machine import SPI, Pin
import tinypico as TinyPICO
from micropython_dotstar import DotStar
import time, random, micropython, gc

print("\n=== mpy-power-test starting\n")

print("Battery Voltage is {}V".format( TinyPICO.get_battery_voltage() ) )
print("Battery Charge State is {}\n".format( TinyPICO.get_battery_charging() ) )
# micropython.mem_info()

# import range
