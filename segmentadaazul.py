import numpy as np
import cv2

# Variaveis globais
cx = 0.0  # Posicao x do retangulo
cy = 0.0  # Posicao y do retangulo
angle = 0.0  # Angulo de rotacao do retangulo,

cap = cv2.VideoCapture(1)

while True:

    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lim_inf = np.array([100, 100, 100])
    lim_sup = np.array([140, 255, 255])

    color_mask = cv2.inRange(hsv, lim_inf, lim_sup)

    (couts, hir) = cv2.findContours(color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cout in couts:
        area = cv2.contourArea(cout)
        cnt = couts[0]

        if area > 800:
            x, y, w, h = cv2.boundingRect(cout)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
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

        #    def draw_angled_rec(x0, y0, width, height, angle, img):
    #
    #                _angle = angle * math.pi / 180.0
    #                b = math.cos(_angle) * 0.5
    #                a = math.sin(_angle) * 0.5
    #                pt0 = (
    #                    int(x0 - a * height - b * width),
    #                    int(y0 + b * height - a * width),
    #                )
    #                pt1 = (
    #                    int(x0 + a * height - b * width),
    #                    int(y0 - b * height - a * width),
    #                )
    #                pt2 = (int(2 * x0 - pt0[0]), int(2 * y0 - pt0[1]))
    #                pt3 = (int(2 * x0 - pt1[0]), int(2 * y0 - pt1[1]))
    #
    #                cv2.line(frame, pt0, pt1, (255, 255, 255), 3)
    #                cv2.line(frame, pt1, pt2, (255, 255, 255), 3)
    #                cv2.line(frame, pt2, pt3, (255, 255, 255), 3)
    #                cv2.line(frame, pt3, pt0, (255, 255, 255), 3)

    #   rows, cols = frame.shape[:2]
    #    [vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
    #    lefty = int((-x * vy / vx) + y)
    #    righty = int(((cols - x) * vy / vx) + y)
    #    cv2.line(frame, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)

    cv2.imshow('Mascara', color_mask)
    cv2.imshow('ObjectDetctionTrack', frame)

    if cv2.waitKey(1) == 27:

        break


cv2.destroyAllWindows()
cap.release()
