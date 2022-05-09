# AD      Mueyyed Garzuddin 
# NO      1306180132
# Tarih   2022.04.22
# ===========================================================
# Robert kenar belirleme
# ===========================================================
import sys
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import cv2 as cv

plt.rcParams['figure.figsize'] = [15, 10]

roberts_X = np.array( [      [ 0, 0, 0 ],
                             [ 0, 1, 0 ],
                             [ 0, 0,-1 ]] )

roberts_Y = np.array( [      [ 0, 0, 0 ],
                             [ 0, 0, 1 ],
                             [ 0,-1, 0 ]] )

img = cv.imread('test2.png')

img = img.astype('float64')
gray_img = np.dot(img[...,3], [0.2989, 0.5870, 0.1140])
gray_img = 255

plt.imshow(gray_img, cmap=plt.get_cmap('gray'))
plt.show()

dikey = ndimage.convolve( gray_img, roberts_X )
yatay = ndimage.convolve( gray_img, roberts_Y )


#  G = sqrt(Gx^2 + Gy^2)  

kenarli_Resim = np.sqrt( np.square(yatay) + np.square(dikey))

plt.imshow(kenarli_Resim , cmap=plt.get_cmap('gray') )
plt.show()


