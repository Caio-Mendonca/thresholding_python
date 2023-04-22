import cv2 
from matplotlib import pyplot as plt


# Calcula o limiar de uma imagem usando o método de Otsu
def calulate_limiar(  img_gray):
    value , otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    plt.imshow(otsu, 'gray')
    plt.savefig('output_otsu.jpg')
    return value 