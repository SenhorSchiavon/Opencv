import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread(r"C:\Users\jd123\github\Opencv\Imagens\einstein.jpg", 0)
imgEqualizada = cv2.equalizeHist(img)
fig = plt.figure(figsize=(20, 5))
ax1 = fig.add_subplot(121)
plt.imshow(img, cmap=plt.cm.gray)


ax2 = fig.add_subplot(122)
plt.imshow(imgEqualizada, cmap=plt.cm.gray)
plt.show()
