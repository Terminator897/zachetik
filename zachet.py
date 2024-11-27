import matplotlib.pyplot as plt
import cv2

nemo = cv2.imread(r"C:\Users\neon6\OneDrive\Новая папка\Рабочий стол\test.jpg")
nemo = cv2.cvtColor(nemo, cv2.COLOR_RGB2HSV)
cv2.waitKey(0)
plt.imshow(nemo)
plt.show()
