import cv2
import numpy as np

#Cargar la imagen a color
IRGB=cv2.imread('004.jpg')
print(IRGB)
print(IRGB.shape)
print("Lineas agregadas en la rama2")
IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print(IGS)
print(IGS.shape)
cv2.imwrite('004GS.jpg',IGS)

