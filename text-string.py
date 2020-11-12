import os
from PIL import Image
import pyautogui
from pytesseract import *

array = []
l = []

print("The available convertable images are: [if you dont find it here please copy-paste the image into the folder of the program]")

for i in os.listdir():
    if i.endswith("png"):
        array.append(i)
        
for pos, i in enumerate(array):
    print(pos, i)
    l.append(pos)
while True:
    ch = int(input("Enter the required image file number shown above:"))
    if ch in l:
        pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        img = Image.open(f"{array[ch]}")
        op = pytesseract.image_to_string(img)
        print(op)
        if input("Press 0 to exit") == "0":
            break
    else:
        print("Wrong input... Try again")

