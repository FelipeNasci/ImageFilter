from Image import Image
from Filters import Filter

img = Image()
filter = Filter()

original = img.getImage()

filter.multiplicativeBrightness(original, 0)
img.showImage("Image Band B", original)
