import network, time
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
time.sleep_ms(100)
print("wifi isConnected=", wifi.isconnected())
if not wifi.isconnected():
    print('connecting to tve-home...')
    wifi.connect('tve-home', 'tve@home')
    while not wifi.isconnected():
        time.sleep_ms(20)
    print('network config:', wifi.ifconfig())
