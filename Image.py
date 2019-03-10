#   A classe contem as matrizes de imagens -> RGB
import cv2
class Image:

    altura = None
    largura = None

    def __init__(self):
        self.b = 0
        self.g = 1
        self.r = 2

    def getImage(self, name):
        img = cv2.imread("images/" + name)
        self.__class__.altura = img.shape[0]
        self.__class__.largura = img.shape[1]
        return img

    def showImage(self, nome, img):
        cv2.imshow(nome, img)           #   Exibir a imagem
        cv2.waitKey(0)                  #   Faz com que a imagem permaneça visivel até ser fechada
