import cv2

# img =cv2.imread("ela com mediana.jpg",0)
# eq = cv2.equalizeHist(img)
# cv2.imwrite("ela com mediana e equa.jpg",eq)

img =cv2.imread("ela com mediana.jpg",0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_img = clahe.apply(img)
cv2.imwrite("ela com mediana e clahe.jpg", clahe_img)