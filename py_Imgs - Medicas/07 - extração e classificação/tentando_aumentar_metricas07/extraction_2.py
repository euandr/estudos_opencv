import mahotas
import os
import pandas
import numpy
import glob
import cv2

labels = ['EOSINOPHIL', 'NEUTROPHIL']

features_list = list()

base_path = r'C:\Users\andre\Documents\atividade\estudos_opencv\processamento de imagens\06-separando_ComBasenosNomes\so_duas_07\\'
# if os.path.exists(base_path):
#     print("O caminho da pasta existe.")
# else:
#     print("O caminho da pasta não existe.")

for label in labels: 
    
    path = base_path + label

    images_list = glob.glob(path + '/*.jpg')

    for image_path in images_list: # usado para passar por cada imagen da pasta.

        img = cv2.imread(image_path, 0)

        if 'NEUTROPHIL' in image_path: label = 1
        if 'EOSINOPHIL' in image_path: label = 0

        
                # ate aqui, tudo pronto, eu acho!

        features_img = mahotas.features.haralick(img, compute_14th_feature = True, return_mean = True)

        features_img = numpy.append(features_img, label)

        features_list.append(features_img)

features_names = mahotas.features.texture.haralick_labels

features_names = numpy.append(features_names, 'Label')

saida_csv = r'C:\Users\andre\Documents\atividade\estudos_opencv\processamento de imagens\07 - extração e classificação\\dados2.csv'

df = pandas.DataFrame(data = features_list, columns = features_names)



df.to_csv(saida_csv, index = False, sep = ';')

    
