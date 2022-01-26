import cv2  # importa tudo

imagem = "Imagens\download.jfif"

image = cv2.imread(imagem)
cv2.imshow('Imagem', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
