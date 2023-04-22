import cv2 

from all_methods import limiarizacao
from calculate_limiar import calulate_limiar

img = cv2.imread('public/moedas01.jpg')
# Converte a imagem para o padrão GRAY
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

limiar = calulate_limiar(img_gray) # 0 - 255

limiarizacao( img, limiar, img_gray)

