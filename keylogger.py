#!/usr/bin/python3

import pynput.keyboard as Keyboard

LOGFILE='/home/laozi/Manas/LIFE/MONEY/WebServer/supervisor/keys.log'

def on_press(key):
    print(str(key).split('.')[-1]+' ', end=' ', flush=True)

with Keyboard.Listener(on_press=on_press) as listener:
    listener.join()