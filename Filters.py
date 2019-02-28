#   A classe contem os filtros a serem aplicados na imagem
class Filter:

    #   Define os tons de cinza com relacao a banda R
    def grayScaleR(self, img):
        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                img [i][l][0] = img [i][l][2]
                img [i][l][1] = img [i][l][2]
        return img

    #   Define os tons de cinza com relacao a banda G
    def grayScaleG(self, img):
        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                img[i][l][2] = img[i][l][1]
                img[i][l][0] = img[i][l][1]
        return img

    #   Define os tons de cinza com relacao a banda B
    def grayScaleB(self, img):
        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                img[i][l][1] = img[i][l][0]
                img[i][l][2] = img[i][l][0]
        return img

    #   Retorna a imagem apenas com banda R
    def bandR(self, img):
        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                img[i][l][0] = 0
                img[i][l][1] = 0
        return img

    #   Retorna a imagem apenas com banda G
    def bandG(self, img):
        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                img[i][l][0] = 0
                img[i][l][2] = 0
        return img

    #   Retorna a imagem apenas com banda B
    def bandB(self, img):
        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                img[i][l][1] = 0
                img[i][l][2] = 0
        return img