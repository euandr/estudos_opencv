import cv2

img = cv2.imread("detectarglobuos/celula.jpg")
cv2.imshow("original",img)
cv2.waitKey(0)


#                    divisao dos tres canais 
canal_B,canal_G,canal_R = cv2.split(img)

#                   clahe em cada canal
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))  
clahe_B = clahe.apply(canal_B)
clahe_G = clahe.apply(canal_G)
clahe_R = clahe.apply(canal_R)

juntando=cv2.merge((clahe_B,clahe_G,clahe_R))
# cv2.imwrite("clahe_canais.jpg",juntando)

bilateral = cv2.bilateralFilter(juntando, d=9, sigmaColor=75, sigmaSpace=75)
# cv2.imwrite("bilateral.jpg",bilateral)
cv2.imshow("clahe em cada canal + bilateral",bilateral)
cv2.waitKey(0)



#               TENTANDO SUBTRAI CANAS R G

canal_R, canal_G,canal_B  = cv2.split(bilateral)

#               subtraçao com cv2
subtracao = cv2.subtract(canal_R,canal_G)
mediana = cv2.medianBlur(subtracao,3)

cv2.imshow("subtracaoRG + mediana",mediana)
cv2.waitKey(0)


_, limiarizada_otsu = cv2.threshold(mediana, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow("Imagem Limiarizada", limiarizada_otsu)
cv2.waitKey(0)


fechamento = cv2.morphologyEx(limiarizada_otsu, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))
cv2.imshow("Fechamento", fechamento)
cv2.waitKey(0)




contornos, _ = cv2.findContours(fechamento, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
maior_contorno = max(contornos, key=cv2.contourArea)


x, y, w, h = cv2.boundingRect(maior_contorno)

inicio = (x - 10, y - 10)
fim = (x + w + 10, y + h + 10)
cv2.rectangle(fechamento, inicio, fim, (255, 255, 255), 4)

cv2.imshow("Caixa na Celula", fechamento)
cv2.waitKey(0)

#quadrado = img[y1:y2 , x1:x2]
quadrado = img[y-10:y+h+10, x-10:x+w+10]
cv2.imshow('Quadrado Extraído', quadrado)
cv2.waitKey(0)


