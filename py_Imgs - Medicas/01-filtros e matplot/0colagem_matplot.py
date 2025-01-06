import cv2
import matplotlib.pyplot as plt

# Carregar as imagens
img1 = cv2.imread("Imagens/elas.png")
img2 = cv2.imread("Imagens/face3.jpg")
img3 = cv2.imread("Imagens/faces.jpg")
img4 = cv2.imread("Imagens/nova.png")

# Converter BGR para RGB
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)

# Exibir as imagens
fig, axs = plt.subplots(5, 5, figsize=(7, 4))

axs[0, 0].imshow(img1)
axs[0, 0].set_title('Imagem 1')
axs[0, 0].axis('off')

axs[0, 1].imshow(img2)
axs[0, 1].set_title('Imagem 2')
axs[0, 1].axis('off')

axs[1, 0].imshow(img3)
axs[1, 0].set_title('Imagem 3')
axs[1, 0].axis('off')

axs[1, 1].imshow(img4)
axs[1, 1].set_title('Imagem 4')
axs[1, 1].axis('off')


axs [3,2].imshow(img1)
axs[3, 2].set_title('Imagem 4')
axs[3, 2].axis('off')
plt.show()
