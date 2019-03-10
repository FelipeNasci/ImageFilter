from Image import Image
from Filters import Filter

img = Image()
filter = Filter()

original = img.getImage("abstract1.jpg")
grayScale = filter.limiarizationRGB(original, 128)

img.showImage("Image Band B", original)
img.showImage("Tons de cinza media 03 bandas", grayScale)
