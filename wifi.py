import network, time
from wifi_pass import wifi_pass # needs to contain one line: wifi_pass='password'
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
time.sleep_ms(100)
print("wifi isConnected=", wifi.isconnected())
if not wifi.isconnected():
    print('connecting to tve-home...')
    wifi.connect('tve-home', wifi_pass)
    while not wifi.isconnected():
        time.sleep_ms(20)
    print('network config:', wifi.ifconfig())
