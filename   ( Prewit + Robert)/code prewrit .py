
# # AD    :  Mueyyed Garzuddin 
# # NO    :  1306180132
# # Tarih :  2022.04.18

# ===========================================================
# Prewit belirleme
# ===========================================================
import cv2
import math
import numpy as np 
from matplotlib import pyplot as plt

class Prewitt:
    def __init__(self, imageName) -> None:
        self.imageName = imageName

    def __veriUretme(self, img):     
        prewittX = [
            [-1,  0,  1],
            [-1,  0,  1],
            [-1,  0,  1]
        ]
        prewittY = [
            [-1, -1, -1],
            [ 0,  0,  0],
            [ 1,  1,  1]
        ]
        
        genislik, yukseklik = img.shape

        pikseller = np.zeros((int(genislik), int(yukseklik)))
        
        for satir in range(genislik - len(prewittX)):
            for sutun in range(yukseklik - len(prewittX)):
                Gx = 0
                Gy = 0
                
                for i in range(len(prewittX)):
                    for j in range(len(prewittY)):
                        deger = img[satir + i, sutun + j]
                        Gx += prewittX[i][j] * deger
                        Gy += prewittY[i][j] * deger
                pikseller[satir + 1, sutun + 1] = int(math.sqrt((Gx * Gx) + (Gy * Gy)))
        return pikseller

    def uretme(self):    
        img = cv2.imread(self.imageName, cv2.IMREAD_GRAYSCALE)

        tumVeri = self.__veriUretme(img)

        fig, eksenler = plt.subplots(
            ncols=2, sharex=True, sharey=True, figsize=(8, 4)
        )
        eksenler[0].imshow(img, cmap=plt.cm.gray)
        eksenler[0].set_title('Asil Goruntu')
        eksenler[1].imshow(tumVeri, cmap=plt.cm.gray)
        eksenler[1].set_title('Prewitt mask ile islenen goruntu')
        for ax in eksenler:
            ax.axis('off')
        plt.tight_layout()
        
# burada ana fonksiyon ( main _ )
prewitt = Prewitt('robert.png')
prewitt.uretme()
 



