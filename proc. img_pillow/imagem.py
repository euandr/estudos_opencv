# from PIL import Image
import PIL.Image as pl


img1= pl.open("img/teste1.jpeg")
img1.show()

# operacoes com imagem
gray_img = img1.convert('L')
gray_img.show()

r,b,g = img1.split()


r.show()

