# config.py Local configuration for mqtt_as demo programs.
from sys import platform
from mqtt_as import config
from led import dotstar

config['server'] = '192.168.0.14'

config['ssid'] = 'tve-home'
config['wifi_pw'] = 'tve@home'

# For demos ensure the same calling convention for LED's on all platforms.
# ESP8266 Feather Huzzah reference board has active low LED's on pins 0 and 2.
# ESP32 is assumed to have user supplied active low LED's on same pins.
# Call with blue_led(True) to light

if platform == 'esp8266' or platform == 'esp32' or platform == 'esp32_LoBo':
    color = [255, 0, 0]
    def set_red(v):
        color[0] = 255 if v else 0
        dotstar[0] = color
    def set_blue(v):
        color[2] = 255 if v else 0
        dotstar[0] = color
    wifi_led = set_red  # Red LED for WiFi fail/not ready yet
    blue_led = set_blue # Message received
elif platform == 'pyboard':
    from pyb import LED
    def ledfunc(led, init):
        led = led
        led.on() if init else led.off()
        def func(v):
            led.on() if v else led.off()
        return func
    wifi_led = ledfunc(LED(1), 1)
    blue_led = ledfunc(LED(3), 0)
