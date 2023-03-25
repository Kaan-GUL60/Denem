import cv2 # opencv kütüphanesini ekleme
import numpy

resim = cv2.imread('test5.png')

# resim okuma işlemi.
cv2.imshow('test5',resim)

# resmi gösterme.
kesilenResim= resim[1:404,351:703]

# resmin istenen sırasıyla y ve x eksenlerini alma
cv2.imshow('kesilenResim',kesilenResim)
cv2.imwrite('kesilenResim3.png',kesilenResim)
# resmi gösterme.
cv2.waitKey()

# gösterilen resmin kapanmasını engelleme. 

img = cv2.imread('test5.png')
ims = cv2.imread('kesilenResim.png')
#verticalAppendedImg = numpy.vstack((img,ims))
horizontalAppendedImg = numpy.hstack((img,ims,ims))
#cv2.imshow('Vertical Appended', verticalAppendedImg)
cv2.imshow('Horizontal Appended', horizontalAppendedImg)
