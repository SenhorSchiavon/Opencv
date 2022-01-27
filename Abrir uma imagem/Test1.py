import cv2  # importa toda a biblioteca cv2

imagem = "download.jfif"

image = cv2.imread(imagem)
cv2.imshow('Imagem', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
