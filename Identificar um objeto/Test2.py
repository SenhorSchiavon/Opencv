import cv2  # Para conseguir programar com OpenCV
from matplotlib import pyplot as plt  # importa o framework

img = cv2.imread("image28.jpg")  # chama a imagem parao arquivo
img_gray = cv2.cvtColor(
    img, cv2.COLOR_BGR2GRAY
)  # Aqui, usa pra transformar a imagem em cinza, o padrão RGB vira BRG e esse é o código do cinza
img_rgb = cv2.cvtColor(
    img, cv2.COLOR_BGR2RGB
)  # Aqui, ele pega e transforma a imagem em colorido novamente.
stop_data = cv2.CascadeClassifier(
    'stop_data.xml'
)  # é o filtro que vê com base nas imagens positivas e negativas


found = stop_data.detectMultiScale(img_gray, minSize=(20, 20))  # Para encontrar a placa
amount_found = len(found)

if amount_found != 0:  # Caso tenha uma placa, vai seguir o if.

    for (x, y, width, height) in found:

        cv2.rectangle(img_rgb, (x, y), (x + height, y + width), (0, 255, 0), 5)

plt.subplot(1, 1, 1)  # Organiza como a imagem vai ser mostrada na tela que irá abrir.
plt.imshow(img_rgb)  # mostra a imagem, se eu colocasse img_gray, ficaria cinza
plt.show()  # Da a ordem pra mostrar
