import csv
import cv2
import glob
import os

pastacomfotos = 'c:\\Users\\andre\\Pictures\\imagens_processadas'
NEUTRO = "C:\\Users\\andre\\Documents\\atividade\\teste\\opencv\\6-separando_ComBasenosNomes\\NEUTROPHIL"
BASO = 'C:\\Users\\andre\\Documents\\atividade\\teste\\opencv\\6-separando_ComBasenosNomes\\BASOPHIL'
EOSINO = "C:\\Users\\andre\\Documents\\atividade\\teste\\opencv\\6-separando_ComBasenosNomes\\EOSINOPHIL"
MONO = "C:\\Users\\andre\\Documents\\atividade\\teste\\opencv\\6-separando_ComBasenosNomes\\MONOCYTE"
LYMPHO = "C:\\Users\\andre\\Documents\\atividade\\teste\\opencv\\6-separando_ComBasenosNomes\\LYMPHOCYTE"
COM_DOIS_NOMES = "C:\\Users\\andre\\Documents\\atividade\\teste\\opencv\\6-separando_ComBasenosNomes\\COM DOIS NOMES"



with open('labels.csv', 'r', encoding="utf8") as arquivo:
    lendo = csv.reader(arquivo)
    next(lendo)  


    for linha in lendo:
        nome = linha[2].strip()

        if not nome:                                                    # Se o nome estiver vazio(44 nomes vazios)
            continue
        else:
    
            nomeimagem = f'BloodImage_{linha[1].zfill(5)}.jpg'
            caminhoimagem = os.path.join(pastacomfotos, nomeimagem)

            if not os.path.isfile(caminhoimagem): 
                print(f"Imagem não encontrada: {nomeimagem}")
                continue

            img = cv2.imread(caminhoimagem)

            if ',' in nome:  
                salvarpasta = COM_DOIS_NOMES
                nomeimagem = f'{nome}.jpg' 
            else:

                if nome == "NEUTROPHIL":
                    salvarpasta = NEUTRO
                elif nome == "BASOPHIL":
                    salvarpasta = BASO
                elif nome == "EOSINOPHIL":
                    salvarpasta = EOSINO
                elif nome == "MONOCYTE":
                    salvarpasta = MONO
                elif nome == "LYMPHOCYTE":
                    salvarpasta = LYMPHO

            # Salvando
            salvasaida = os.path.join(salvarpasta, nomeimagem)
            cv2.imwrite(salvasaida, img)
            print(f"\033[;32mImagem movida para: {salvasaida}\033[m")
          