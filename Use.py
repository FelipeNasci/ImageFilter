from Image import Image
from Filters import Filter

img = Image()
filter = Filter()

original = img.getImage()

filter.bandB(original)
img.showImage("Image Band B", original)
