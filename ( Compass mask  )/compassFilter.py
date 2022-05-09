# AD    :  Mueyyed Garzuddin 
# NO    :  1306180132
# Tarih :  2022.04.18

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import cv2


GriGoruntu = cv2.imread("compass.png",0)
cv2.imshow("GriGoruntu2",GriGoruntu)

h, w = GriGoruntu.shape #assigning height and width of the image to h&w
Sonuc = np.zeros((h, w)) #creating an array of zeros, size is [h][w]
Sonuc0 = np.array([[-1, -1, -1], [+1, -2, 1], [1, 1, 1]])  #yukseklik degiskene atanma 
Sonuc45 = np.array([[-1, -1, 1], [-1, -2, 1], [1, 1, 1]])   
Sonuc90 = np.array([[-1, 1, 1], [-1, -2, 1], [-1, 1, 1]])   
Sonuc135 = np.array([[1, 1, 1], [-1, -2, 1], [-1, -1, 1]])  
Sonuc180 = np.array([[1, 1, 1], [1, -2, 1], [-1, -1, -1]]) 
Sonuc225 = np.array([[1, 1, 1], [1, -2, -1], [1, -1, -1]]) 
Sonuc270 = np.array([[1, 1, -1], [1, -2, -1], [1, 1, -1]])  
Sonuc315 = np.array([[1, -1, -1], [1, -2, -1], [1, 1, 1]])  


def ImageG(GriGoruntu,filtre,i,j): #gri goruntuya filtre uygualanabilmek icin kullanilen bir fonksiyondur
    return    (filtre[0, 0] * GriGoruntu[i - 1, j - 1]) +(filtre[0, 1] * GriGoruntu[i - 1, j]) +(filtre[0, 2] * GriGoruntu[i - 1, j + 1]) + \
              (filtre[1, 0] * GriGoruntu[i, j - 1]) + (filtre[1, 1] * GriGoruntu[i, j]) +(filtre[1, 2] * GriGoruntu[i, j + 1]) + \
              (filtre[2, 0] * GriGoruntu[i + 1, j - 1]) +(filtre[2, 1] * GriGoruntu[i + 1, j]) + (filtre[2, 2] * GriGoruntu[i + 1, j + 1])




for i in range(1, h - 1):
    for j in range(1, w - 1):

        Sonuc[i - 1, j - 1] = max(abs(ImageG(GriGoruntu,Sonuc0,i,j)),abs(ImageG(GriGoruntu,Sonuc45,i,j)), #maks filtre sonucu .
                                   abs(ImageG(GriGoruntu,Sonuc90,i,j)),abs(ImageG(GriGoruntu,Sonuc135,i,j)),
                                   abs(ImageG(GriGoruntu,Sonuc180,i,j)),abs(ImageG(GriGoruntu,Sonuc225,i,j)),
                                   abs(ImageG(GriGoruntu,Sonuc270,i,j)),abs(ImageG(GriGoruntu,Sonuc315,i,j)))


    #kullanciya sonuc gostermek 
plt.figure()
plt.title('compassSonuc')
plt.imshow(Sonuc, cmap='gray')
plt.show()