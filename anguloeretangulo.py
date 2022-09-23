import numpy as np
import cv2
import sys
import yaml
import os
import warnings

warnings.filterwarnings("ignore")

# Variaveis globais
cx = 0.0  # Posicao x do retangulo
cy = 0.0  # Posicao y do retangulo
angle = 0.0  # Angulo de rotacao do retangulo

if __name__ == "__main__":
    while 1:
        try:
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

            while 1:
                _, frame = cap.read()
                k = cv2.waitKey(5)
                if k == 27:  # esc pra sair
                    cv2.destroyAllWindows()
                    sys.exit()
                if k == 13:  # Salvar o centroide
                    result_file = r'rectangle_position.yaml'
                    try:
                        os.remove(result_file)  # Deleta o arquivo antigo
                    except:
                        pass
                    print("Saving Rectangle Position Matrix in: ", result_file)
                    data = {"rect_position": [cx, cy, angle]}
                    with open(result_file, "w") as f:
                        yaml.dump(data, f, default_flow_style=False)

                # Vamos ter que pegar o RGB, inicialmente cor azul
                red = np.matrix(frame[:, :, 2])  # Pegando  cor vermelha
                green = np.matrix(frame[:, :, 1])  # Pegando a cor verde
                blue = np.matrix(frame[:, :, 0])
                # Comecar a preparar a mask com o blue
                blue_only = np.int16(blue) - np.int16(red) - np.int16(green)
                blue_only[blue_only < 0] = 0
                blue_only[blue_only > 255] = 255
                blue_only = np.uint8(blue_only)

                # Filtro Gaussiano
                blur = cv2.GaussianBlur(blue_only, (5, 5), cv2.BORDER_DEFAULT)
                # thresh hold e o que faz pra procurar o angulo
                ret3, thresh = cv2.threshold(
                    blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
                )
                cv2.namedWindow('Threshold', cv2.WINDOW_AUTOSIZE)
                cv2.imshow("Threshold", thresh)
                cv2.waitKey(1)
                # Procurando o contorno dos objetos e encontrar o retangulo
                contours, hierarchy = cv2.findContours(
                    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE
                )

                for contour in contours:
                    area = cv2.contourArea(contour)
                    if area > 10000:
                        contours.remove(contour)

                cnt = contours[0]

                rotatedRect = cv2.minAreaRect(cnt)
                # pegando centroide, comprimento, largura e anglo do retangulo
                (cx, cy), (width, height), angle = rotatedRect
                cx = int(cx)
                cy = int(cy)
                print(cx, cy)  # mostra os valores de x e y

                if width > height:
                    angle = angle + 180
                else:
                    angle = angle + 90
                print("Angle b/w shorter side with Image Vertical: \n", angle)

                # Desenhar o retangulo ao redor
                # https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contours_begin/py_contours_begin.html#how-to-draw-the-contours
                im = cv2.drawContours(frame, [cnt], 0, (0, 0, 255), 2)
                cv2.circle(im, (cx, cy), 2, (200, 255, 0), 2)  # desenha o circulo
                cv2.putText(
                    im,
                    str("Angle: " + str(int(angle))),
                    (int(cx) - 40, int(cy) + 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 0, 255),
                    1,
                    cv2.LINE_AA,
                )
                cv2.putText(
                    im,
                    str("Center: " + str(cx) + "," + str(cy)),
                    (int(cx) - 40, int(cy) - 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 0, 255),
                    1,
                    cv2.LINE_AA,
                )
                cv2.namedWindow('Detected Rect', cv2.WINDOW_AUTOSIZE)
                cv2.imshow('Detected Rect', im)
                cv2.waitKey(1)

        except Exception as e:
            print("Error in Main Loop\n", e)
            cv2.destroyAllWindows()
            sys.exit()

    cv2.destroyAllWindows()
