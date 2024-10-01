import PIL.Image as p
import glob

# caminho = r"C:\PythonSM\proc. img_pillow\img\*.*"
caminho = "img/*.*"

for img in glob.glob(caminho):
   carregando = p.open(img)
   carregando.show()