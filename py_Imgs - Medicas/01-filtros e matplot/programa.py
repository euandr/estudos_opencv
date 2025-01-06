
import cv2

#         # media
# imagem = cv2.imread("ela.jpg")
# media = cv2.blur(imagem, (3,3))
# cv2.imwrite("filtro media.png",media)

#          #mediana
# mediana = cv2.medianBlur(imagem,3)
# cv2.imwrite("ela com mediana.jpg",mediana)


#         #Gaussiana
# img = cv2.imread("ela.jpg")
# imagem_suavizada = cv2.GaussianBlur(img, (3, 3), 0)
# cv2.imwrite("ela com gaussiana.jpg",imagem_suavizada)

#         #equalizacao
# img = cv2.imread("ela.jpg",0)
# eq = cv2.equalizeHist(img)
# cv2.imwrite("ela com equalizacao.jpg",eq)

# #         clahe
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
# clahe_img = clahe.apply(img)
# cv2.imwrite("ela com clahe.jpg", clahe_img)
