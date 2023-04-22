import cv2 
import numpy as np
from matplotlib import pyplot as plt


def limiarizacao( img, limiar, gray):
    # Métodos de limiarização
    _ , thresh_binary = cv2.threshold(gray, limiar, 255, cv2.THRESH_BINARY)
    _ , thresh_binary_inv = cv2.threshold(gray, limiar, 255, cv2.THRESH_BINARY_INV)
    _ , thresh_trunc = cv2.threshold(gray, limiar, 255, cv2.THRESH_TRUNC)
    _ , thresh_tozero = cv2.threshold(gray, limiar, 255, cv2.THRESH_TOZERO)
    _ , thresh_tozero_inv = cv2.threshold(gray, limiar, 255, cv2.THRESH_TOZERO_INV)
    titulos = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    imagens = [img, thresh_binary, thresh_binary_inv, thresh_trunc, thresh_tozero, thresh_tozero_inv]

    fig  = plt.gcf()
    fig.set_size_inches(18.5, 10.5)

    for i in range(6):
        plt.subplot(2, 3, i+1), plt.imshow(imagens[i], 'gray')
        plt.title(titulos[i])
        plt.xticks([]),plt.yticks([])
    
    plt.savefig('output.jpg')

