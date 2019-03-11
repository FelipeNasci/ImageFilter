from Image import Image
from Filters import Filter

img = Image()
img2 = Image()
filter = Filter()

#   Limiarização
'''
original = img.getImage("anciao.jpg")
filtrada = filter.limiarizationRGB(original, 160)

img.showImage("Original Image", original)
img.showImage("Limiarizacao", filtrada)
'''

#   NegativoRGB
'''
original = img.getImage("anciao.jpg")

negativeRGB = filter.negative(original)
negativeB = filter.negativeRGB(original, 0)
negativeG = filter.negativeRGB(original, 1)
negativeR = filter.negativeRGB(original, 2)

img.showImage("Negativo em RGB", negativeRGB)
img.showImage("Negativo em B", negativeB)
img.showImage("Negativo em G", negativeG)
img.showImage("Negativo em R", negativeR)
'''

'''
#   NegativoY
original = img.getImage("model.jpg")
negativeY = filter.negative(original)
img.showImage("Negativo em Y", original)
'''

#   brilho Aditivo
'''
original = img.getImage("anciao.jpg")

brilhoAditivo0 = filter.additiveBrightnessRGB(original, 0)
brilhoAditivo128 = filter.additiveBrightnessRGB(original, 128)
brilhoAditivo255 = filter.additiveBrightnessRGB(original, 255)

#       Escurecendo a imagem
brilhoAditivo128neg = filter.additiveBrightnessRGB(original, -128)
brilhoAditivo255neg = filter.additiveBrightnessRGB(original, -255)

img.showImage("Original Image", original)
img.showImage("Brilho aditivo com C = 0", brilhoAditivo0)
img.showImage("Brilho aditivo com C = 128", brilhoAditivo128)
img.showImage("Brilho aditivo com C = 255", brilhoAditivo255)
img.showImage("Brilho aditivo com C = -128", brilhoAditivo128neg)
img.showImage("Brilho aditivo com C = -255", brilhoAditivo255neg)
img.showImage("Brilho aditivo com C = 128 depois C = -128", filter.additiveBrightnessRGB(filter.additiveBrightnessRGB(original, 128), -128))
'''

#   Brilho multiplicativo
'''
original = img.getImage("anciao.jpg")

for i in range (0,10):
    brilhoMultiply0 = filter.multiplicativeBrightnessRGB(original, i)
    s = "Brilho multiplicativo com C = {}".format(i)
    img.showImage(s, brilhoMultiply0)
'''

#   Media
original = img.getImage("Shapes.png")
filtrada = filter.negative(original)

img.showImage("Original Image", original)
img2.showImage("Limiarizacao", filtrada)
