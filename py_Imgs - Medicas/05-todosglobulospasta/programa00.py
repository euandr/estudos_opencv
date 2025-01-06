import cv2
import glob
import os

pastacomfotos = 'c:\\Users\\andre\\Pictures\\JPEGImages'
saida = 'c:\\Users\\andre\\Pictures\\imagens_processadas'

lista_arquivos = glob.glob(os.path.join(pastacomfotos, '*.*'))

for caminho_img in lista_arquivos:

    img = cv2.imread(caminho_img)
    
    if img is None:
        continue  # Pule se a imagem não for lida corretamente

    # Divisão dos três canais
    canal_B, canal_G, canal_R = cv2.split(img)

    # CLAHE em cada canal
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe_B = clahe.apply(canal_B)
    clahe_G = clahe.apply(canal_G)
    clahe_R = clahe.apply(canal_R)

    juntando = cv2.merge((clahe_B, clahe_G, clahe_R))

    bilateral = cv2.bilateralFilter(juntando, d=9, sigmaColor=75, sigmaSpace=75)

    #              TENTANDO Subtrair os canais R e G
    canal_R, canal_G, canal_B = cv2.split(bilateral)
    subtracao = cv2.subtract(canal_R, canal_G)
    mediana = cv2.medianBlur(subtracao, 3)


    _, limiarizada_otsu = cv2.threshold(mediana, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    fechamento = cv2.morphologyEx(limiarizada_otsu, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))

    contornos, _ = cv2.findContours(fechamento, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contornos:
        continue  

    maior_contorno = max(contornos, key=cv2.contourArea)

    x, y, w, h = cv2.boundingRect(maior_contorno)

    inicio = (x - 10, y - 10)
    fim = (x + w + 10, y + h + 10)
    
    inicio = (max(inicio[0], 0), max(inicio[1], 0))
    fim = (min(fim[0], img.shape[1]), min(fim[1], img.shape[0]))

    cv2.rectangle(fechamento, inicio, fim, (255, 255, 255), 4)

    quadrado = img[inicio[1]:fim[1], inicio[0]:fim[0]]

    nomearquivo = os.path.basename(caminho_img)
    salvasaida = os.path.join(saida, nomearquivo)

    cv2.imwrite(salvasaida, quadrado)
