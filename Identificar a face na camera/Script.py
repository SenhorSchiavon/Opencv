import cv2

camera = cv2.VideoCapture(0) #Captura a câmera integrada ao pc.
videoface = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    cam, frame = camera.read()  # vai ler a camera por frame
    cameracinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#Existe uma preferência pela foto cinza no desempenho
    detectarface = videoface.detectMultiScale(cameracinza)
    for (x, y, w, z) in detectarface:#Fazer retângulos nas faces encontradas.
        cv2.rectangle(frame, (x, y), (x + w, y + z), (0, 255, 255), 2)
    cv2.imshow("Video da câmera", frame)
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()#Deixa a câmera rodando
cv2.destroyAllWindows() #Fecha a janela aberta.
