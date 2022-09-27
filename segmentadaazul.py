import numpy as np #biblioteca
import cv2 #biblioteca

cap = cv2.VideoCapture(0) #Definir a captura do video na camera 0

while True:

    ret, frame = cap.read() #Vai ler o proximo frame e ret vai retornar o valor do frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Mascara pra melhor definicao

    lim_inf = np.array([100, 100, 100])  #Range da paleta
    lim_sup = np.array([140, 255, 255])  #Range da paleta

    color_mask = cv2.inRange(hsv, lim_inf, lim_sup) #Definindo limites de cores

    (couts, hir) = cv2.findContours(color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #Procurando contornos

    for cout in couts:
        area = cv2.contourArea(cout) #Ele vai contornar a area que se encaixa nas definicoes a cima

        if area > 800:
            x, y, w, h = cv2.boundingRect(cout)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) #Se a area for maior que 800 pixels, se encaixa no nosso padrao e vai desenhar circulo

    cv2.imshow('Mascara', color_mask) #Vai abrir uma janela pra mascara
    cv2.imshow('ObjectDetctionTrack', frame) #Vai abrir uma janela pra camera

    if cv2.waitKey(1) == 27:
        break #Pressionar Esc desliga o sistema

cv2.destroyAllWindows() #Fecha as janelas abertas
cap.release() #Para com a camera
