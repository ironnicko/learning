import os
from PIL import Image
#os.system("pip install pytesseract")
import pyautogui
from pytesseract import *

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open("views.png")
op = pytesseract.image_to_string(img, lang="fra")

print(op)
