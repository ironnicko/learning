import pyqrcode

s = input('Enter the text or URL:')
name = input('Enter the name of the file:')
url = pyqrcode.create(s)
url.png(f'{name}.png', scale=6)
