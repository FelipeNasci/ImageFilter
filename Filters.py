from copy import copy
import math

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
    
    #   Retorna a imagem com as bandas em negativo
    def negativeRGB(self, img):
        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                img[i][l][0] = 255 - img[i][l][0]
                img[i][l][1] = 255 - img[i][l][1]
                img[i][l][2] = 255 - img[i][l][2]
        return img
    
    #   Retorna a imagem com todos os pixels + c
    def additiveBrightness(self, img, c):
        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                aux = img[i][l][0] + c
                if (aux > 255):
                    img[i][l][0] = 255
                else:
                    img[i][l][0] = aux
                
                aux = img[i][l][1] + c
                if (aux > 255):
                    img[i][l][1] = 255
                else:
                    img[i][l][1] = aux

                aux = img[i][l][2] + c
                if (aux > 255):
                    img[i][l][2] = 255
                else:
                    img[i][l][2] = aux                         
        return img
    
    #   Retorna a imagem com todos os pixels * c
    def multiplicativeBrightness(self, img, c):
        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                aux = img[i][l][0] * c
                if (aux > 255):
                    img[i][l][0] = 255
                else:
                    img[i][l][0] = aux
                
                aux = img[i][l][1] * c
                if (aux > 255):
                    img[i][l][1] = 255
                else:
                    img[i][l][1] = aux
                
                aux = img[i][l][2] * c
                if (aux > 255):
                    img[i][l][2] = 255
                else:
                    img[i][l][2] = aux                         
        return img
    
    #   Aplica o filtro da mediana em uma copia da imagem
    #   raio = o raio da mascara. ex: raio = 3, mascara 5x5
    def medianaRGB(self, img, raio):
        imgAux = copy(img)
        subMatrixB = []
        subMatrixG = []
        subMatrixR = []
        #varre cada pixel da imagem com os limites sem extensao por zero
        for i in range(raio-1, len(img)-(raio-1)):
            for l in range(raio-1, len(img[0])-(raio-1)):
                #submatriz para o filtro em cada pixel
                subMatrix = img[i-raio+1:i+raio , l-raio+1:l+raio]
                
                #separa as informações das bandas
                for a in range(0, len(subMatrix)):
                    for b in range(0, len(subMatrix[0])):
                        subMatrixB.append(subMatrix[a][b][0])
                        subMatrixG.append(subMatrix[a][b][1])
                        subMatrixR.append(subMatrix[a][b][2])
                
                #ordena os valores das bandas e pega o do meio para colocar na imagem
                subMatrixB.sort()
                subMatrixG.sort()
                subMatrixR.sort()
                imgAux[i][l][0] = subMatrixB[math.trunc(len(subMatrixB)/2)]
                imgAux[i][l][1] = subMatrixG[math.trunc(len(subMatrixG)/2)]
                imgAux[i][l][2] = subMatrixR[math.trunc(len(subMatrixR)/2)]
                subMatrixB = []
                subMatrixG = []
                subMatrixR = []
        #corta as linhas e colunas que não participaram
        imgAux = imgAux[raio-1:len(imgAux)-(raio-1) , raio-1:len(imgAux[0])-(raio-1)]
        return imgAux
                    
