import cv2 as cv

import numpy as np

# # Photos
# im =  cv.imread('ini.png', cv.IMREAD_COLOR)
# cv.imshow("Window",im)
# cv.waitKey(0)
# cv.destroyAllWindows()

# Videos

# video = cv.VideoCapture(0)

# while 1:
#     re, frame = video.read()
#     cv.imshow("video", frame)

#     if cv.waitKey(60) & 0xFF==ord('f'):
#         break
# video.release()
# cv.destroyAllWindows()

# Rescaling

# def rescale_Frame(frame, scale=0.75):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
#     dimensions = (width, height)
#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# im = cv.imread("ini.png", 0)

# rescaled = rescale_Frame(im)

# cv.imshow('rescaled', rescaled)

# video = cv.VideoCapture(0)

# while 1:
#     re, frame = video.read()

#     frame_resized = rescale_Frame(frame)

#     cv.imshow("video", frame)
#     cv.imshow('resized', frame_resized)

#     if cv.waitKey(60) & 0xFF==ord('f'):
#         break
# video.release()
# cv.destroyAllWindows()

# Res of only live videos

# def change_Res(width, height):
#     # only for live

#     video.set(3, width)
#     video.set(4, height)

# video = cv.VideoCapture(0)

# new = change_Res(100, 15)

# while 1:
#     re, frame = video.read()
#     cv.imshow('window', frame)
#     if cv.waitKey(60) & 0xFF==ord('f'):
#         break
# video.release()
# cv.destroyAllWindows()


# ** Drawing and Writing

# black = np.zeros((500, 500, 3))

# black[200:300, 300:400] = 255, 0, 0

# cv.imshow('blue', black)

# cv.rectangle(black, (0,0), (250, 250), (255, 255, 255), thickness=cv.FILLED)
# cv.imshow('Rectangle', black)

# cv.circle(black, (black.shape[1]//2, black.shape[0]//2), 40, (0, 0, 255), thickness=-1)

# cv.imshow('Circle', black)

# cv.line(black, (100, 250), (300, 400), (255, 255, 255), thickness=3)
# cv.imshow('Line', black)

# cv.putText(black, 'Harini', (0, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
# cv.imshow('Text', black)

# cv.waitKey(0)
# cv.destroyAllWindows()

# Very Important basics for computer vision 

# color to grayscale
# im = cv.imread('ini.png', cv.IMREAD_COLOR)
# cv.imshow('window', im)

# grey = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
# cv.imshow('Grey', grey)

# cv.waitKey(0)
# cv.destroyAllWindows()

# Blur
# im = cv.imread('birthday.png')

# cv.imshow('Normal', im)

# blur = cv.GaussianBlur(im, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blurred', blur)

# cv.waitKey(0)
# cv.destroyAllWindows()

# Edge Cascades
# img = cv.imread('ini.png', 0)

# blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)

# canny = cv.Canny(blur, 125, 175)

# # cv.imshow('canny', canny)

# # Dialating the image
# dilated = cv.dilate(canny, (7,7), iterations=5) 

# cv.imshow('Dialated', dilated)

# # Eroding
# eroded = cv.erode(dilated, (7,7), iterations=5)

# cv.imshow('eroded', eroded)


# Resizing

# resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)

# cv.imshow('resized', resize)

# cropped = img[50:200, 200:400]
# cv.imshow('cropped', cropped)

cv.waitKey(0)