#!/usr/bin/python3
import time
import platform
from binance.client import Client 
'''For installing this module : pip3 install python-binance'''

''' 
Check if Raspberry Pi is available, if not use the sense-hat emulator
'''
if(platform.machine()) == "armv7l":
    from sense_hat import SenseHat
else:
    from sense_emu import SenseHat


BINANCE_API_KEY = ""
BINANCE_API_SECRET = ""
client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

def get_prices(ticker):
    i_avg_price = client.get_avg_price(symbol=ticker)['price']
    return int(float(i_avg_price))

sense = SenseHat()
black = (0, 0, 0)
yellow = (255, 255, 0)
while True:
    sense.show_message('BTCEUR: '+str(get_prices('BTCEUR')),text_colour=yellow,back_colour=black)
    sense.show_message('ETHEUR: '+str(get_prices('ETHEUR')),text_colour=yellow,back_colour=black)
    time.sleep(5)
