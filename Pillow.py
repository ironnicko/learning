import os
os.system('pip3 install Pillow')
from PIL import Image, ImageFilter

image = Image.open('something.png')  # image object

image.show()  # to show it

image.save('something.jpeg')  # to convert to any extention/to save

# to convert a list of files to someother format
for i in os.listdir('.'):
    if i.endswith('.jpeg'):
        p = Image.open(i)
        fn, ext = os.path.splitext(i)
        p.save(f'PNG/{fn}.png')

# To convert them into a thumbnail/smaller version
size = (300,300)
size1 = (700,700)
for i in os.listdir('.'):
    if i.endswith('.jpeg'):
        p = Image.open(i)
        fn, ext = os.path.splitext(i)

        p.thumbnail(size)
        p.save(f'PNG/{fn}_300.png')

        p.thumbnail(size1)
        p.save(f'PNG/{fn}_700.png')

# rotating

image = Image.open('something.png') 
image.rotate(90).save('som90.jpg')

# Inverting
image = Image.open('something.png') 
image.convert(mode='L').save('inverted.png')

# Image Filter
image = Image.open('something.png') 
image.filter(ImageFilter.GaussianBlur(10)).save('GaussianBlur.png')

