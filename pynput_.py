import os
os.system('pip3 install pynput')
os.system('pip3 install subprocess')
import pynput, subprocess
from pynput.keyboard import Key, Listener

# print the keys

def on_press(key):
  print(f'{key} was pressed')
  
def on_release(key):
  if key == Key.esc:# Escape closes the program
    return False
with Listener(on_press=on_press, on_release=on_release) as L:
  L.join()
  
# open any application using a hotkey
# make sure to comment the above code before executing this one

PATH = '<path to the application with it's name eg: /home/nikhil/Desktop/VSCode>'

def on_press(key):
  if key == Key.f5:# im using F5 as the hot-key, you can use anything
    subprocess.open(PATH)
  
def on_release(key):# Escape closes the program
  if key == Key.esc:
    return False
with Listener(on_press=on_press, on_release=on_release) as L:
  L.join()
