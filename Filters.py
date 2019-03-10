from copy import copy
import numpy as np
import math

#   A classe contem os filtros e operacoes a serem aplicados em imagens
class Filter:
    
    #   Retorna um array numpy com as mesmas dimensoes da imagem
    #   contendo os valores dos pixels convertidos em YIQ
    def rgbToYiq(self, img):
        YIQ = np.empty((img.shape[0], img.shape[1], img.shape[2]), dtype=float)
        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                Y = 0.299*img[i][l][2] + 0.587*img[i][l][1] + 0.114*img[i][l][0]
                I = 0.596*img[i][l][2] - 0.274*img[i][l][1] - 0.322*img[i][l][0]
                Q = 0.211*img[i][l][2] - 0.523*img[i][l][1] + 0.312*img[i][l][0]
                YIQ[i][l] = [Y, I, Q]
        return YIQ

    #   Retorna um array numpy com as mesmas dimensoes do array YIQ
    #   contendo os valores dos pixels convertidos em RGB
    def yiqToRgb(self, YIQ):
        RGB = np.empty((YIQ.shape[0], YIQ.shape[1], YIQ.shape[2]), dtype=np.uint8)
        for i in range(0, len(YIQ)):
            for l in range(0, len(YIQ[0])):
                #necessario tratar os limites na volta para RGB
                R = round(1.000*YIQ[i][l][0] + 0.956*YIQ[i][l][1] + 0.621*YIQ[i][l][2])
                if (R > 255):
                    R = 255
                elif (R < 0):
                    R = 0

                G = round(1.000*YIQ[i][l][0] - 0.272*YIQ[i][l][1] - 0.647*YIQ[i][l][2])
                if (G > 255):
                    G = 255
                elif (G < 0):
                    G = 0

                B = round(1.000*YIQ[i][l][0] - 1.106*YIQ[i][l][1] + 1.703*YIQ[i][l][2])
                if (B > 255):
                    B = 255
                elif (B < 0):
                    B = 0
                #BGR devido a opencv
                RGB[i][l] = [B, G, R]
        return RGB

    #   Define os tons de cinza com relacao a banda
    def grayScale(self, img, band):
        GRAYSCALE = np.empty((img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8)

        if band > 2 : band = 2
        elif band < 0: band = 0

        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                value = img [i][l][band]
                GRAYSCALE[i][l] = [value, value, value]
        return GRAYSCALE

    #   Retorna a imagem apenas com banda R
    def bandR(self, img):
        RED = np.empty((img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8)
        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                RED[i][l][2] = img[i][l][2]
        return RED

    #   Retorna a imagem apenas com banda G
    def bandG(self, img):
        GREEN = np.empty((img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8)
        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                GREEN[i][l][1] = img[i][l][1]
        return GREEN

    #   Retorna a imagem apenas com banda B
    def bandB(self, img):
        BLUE = np.empty((img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8)
        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                BLUE[i][l][0] = img[i][l][0]
        return BLUE

####################################################################################
################################ NEGATIVO ##########################################
####################################################################################
    #   Retorna a imagem com as bandas em negativo
    def negativeRGB(self, img):
        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                img[i][l][0] = 255 - img[i][l][0]
                img[i][l][1] = 255 - img[i][l][1]
                img[i][l][2] = 255 - img[i][l][2]
        return img
    
    #   Converte a imagem para a banda YIQ, aplica o negativo e converte e volta para RGB
    def negativeY(self, img):
        imgY = self.rgbToYiq(img)
        for i in range(0, len(imgY)):
            for l in range(0, len(imgY[0])):
                imgY[i][l][0] = 255 - imgY[i][l][0]
        return self.yiqToRgb(imgY)
#################################################################################### 

####################################################################################
############################ BRILHO ################################################
####################################################################################
    
    #   Retorna a imagem com todos os pixels + c
    def additiveBrightnessRGB(self, img, c):
        imgAux = copy(img)
        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                #aux usado pois o tipo do array e uint8 (0 - 255)
                aux = img[i][l][0] + c
                if (aux > 255):
                    imgAux[i][l][0] = 255
                else:
                    imgAux[i][l][0] = aux
                
                aux = img[i][l][1] + c
                if (aux > 255):
                    imgAux[i][l][1] = 255
                else:
                    imgAux[i][l][1] = aux

                aux = img[i][l][2] + c
                if (aux > 255):
                    imgAux[i][l][2] = 255
                else:
                    imgAux[i][l][2] = aux                         
        return imgAux
    
    #   Converte uma imagem para YIQ, aplica o brilho na banda Y e retorna para RGB
    def additiveBrightnessY(self, img, c):
        imgY = self.rgbToYiq(img)
        for i in range(0, len(imgY)):
            for l in range(0, len(imgY[0])):
                #aux usado pois o tipo do array e uint8 (0 - 255)
                aux = imgY[i][l][0] + c
                if (aux > 255):
                    imgY[i][l][0] = 255
                else:
                    imgY[i][l][0] = aux
        return self.yiqToRgb(imgY)
    
    #   Retorna a imagem com todos os pixels * c
    def multiplicativeBrightnessRGB(self, img, c):
        imgAux = copy(img)
        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                #aux usado pois o tipo do array e uint8 (0 - 255)
                aux = img[i][l][0] * c
                if (aux > 255):
                    imgAux[i][l][0] = 255
                else:
                    imgAux[i][l][0] = aux
                
                aux = img[i][l][1] * c
                if (aux > 255):
                    imgAux[i][l][1] = 255
                else:
                    imgAux[i][l][1] = aux
                
                aux = img[i][l][2] * c
                if (aux > 255):
                    imgAux[i][l][2] = 255
                else:
                    imgAux[i][l][2] = aux                         
        return imgAux
    
    #   Converte uma imagem para YIQ, aplica o brilho na banda Y e retorna para RGB
    def multiplicativeBrightnessY(self, img, c):
        imgY = self.rgbToYiq(img)
        for i in range(0, len(imgY)):
            for l in range(0, len(imgY[0])):
                #aux usado pois o tipo do array e uint8 (0 - 255)
                aux = imgY[i][l][0] * c
                if (aux > 255):
                    imgY[i][l][0] = 255
                else:
                    imgY[i][l][0] = aux
        return self.yiqToRgb(imgY)
#####################################################################################

#####################################################################################
############################ MEDIANA ################################################
#####################################################################################
    
    #   Aplica o filtro da mediana em uma copia da imagem
    #   raio = o raio da mascara. ex: raio = 3, mascara 5x5
    def medianRGB(self, img, raio):
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
    
    #   Converte uma imagem para YIQ, aplica a mediana na banda Y e converte de volta para RGB
    def medianY(self, img, raio):
        imgY = self.rgbToYiq(img)
        subMatrixY = []
        #varre cada pixel da imagem com os limites sem extensao por zero
        for i in range(raio-1, len(imgY)-(raio-1)):
            for l in range(raio-1, len(imgY[0])-(raio-1)):
                #submatriz para o filtro em cada pixel
                subMatrix = imgY[i-raio+1:i+raio , l-raio+1:l+raio]
                
                #separa as informações da banda Y
                for a in range(0, len(subMatrix)):
                    for b in range(0, len(subMatrix[0])):
                        subMatrixY.append(subMatrix[a][b][0])
                
                #ordena os valores das bandas e pega o do meio para colocar na imagem
                subMatrixY.sort()
                imgY[i][l][0] = subMatrixY[math.trunc(len(subMatrixY)/2)]
                subMatrixY = []
        #corta as linhas e colunas que não participaram
        imgY = imgY[raio-1:len(imgY)-(raio-1) , raio-1:len(imgY[0])-(raio-1)]
        return self.yiqToRgb(imgY)
####################################################################################
    
####################################################################################
######################## CONVOLUCAO E FILTROS ######################################
####################################################################################
    
    #   Aplica uma mascara em uma imagem, multiplicando cada valor da mascara
    #   com o valor do pixel correspondente da imagem
    def convolutionRGB(self, img, mask):
        imgAux = copy(img)
        raio = math.ceil(len(mask)/2)
        opB, opG, opR = 0, 0, 0
        maskI = 0 #representa os indices das linhas da mascara
        maskJ = 0 #representa os indices das colunas da mascara
        #varre cada pixel da imagem com os limites sem extensao por zero
        for i in range(raio-1, len(img)-(raio-1)):
            for l in range(raio-1, len(img[0])-(raio-1)):
                #varre os indices da imagem ao redor do pixel de acordo com a mascara
                for c in range(i-(raio-1), i+(raio)):
                    for k in range(l-(raio-1), l+(raio)):
                        #aplica a mascara em cada banda do pixel
                        opB += (img[c][k][0] * mask[maskI][maskJ])
                        opG += (img[c][k][1] * mask[maskI][maskJ])
                        opR += (img[c][k][2] * mask[maskI][maskJ])
                        maskJ += 1
                    maskJ = 0
                    maskI += 1
                maskI = 0
                imgAux[i][l][0] = round(opB)
                imgAux[i][l][1] = round(opG)
                imgAux[i][l][2] = round(opR)
                
                #verificando os limites de RGB
                if (opB > 255):
                    imgAux[i][l][0] = 255
                elif (opB < 0):
                    imgAux[i][l][0] = 0
                    
                if (opG > 255):
                    imgAux[i][l][1] = 255
                elif (opG < 0):
                    imgAux[i][l][1] = 0
                    
                if (opR > 255):
                    imgAux[i][l][2] = 255
                elif (opR < 0):
                    imgAux[i][l][2] = 0
                
                opB, opG, opR = 0, 0, 0
        return imgAux
    
    #   Aplica uma mascara em uma matriz YIQ, multiplicando cada valor da mascara
    #   com o valor da banda Y do pixel correspondente
    def convolutionY(self, img, mask):
        imgY = self.rgbToYiq(img)
        imgYAux = copy(imgY)
        raio = math.ceil(len(mask)/2)
        opY = 0
        maskI = 0 #representa os indices das linhas da mascara
        maskJ = 0 #representa os indices das colunas da mascara
        #varre cada pixel da imagem com os limites sem extensao por zero
        for i in range(raio-1, len(imgY)-(raio-1)):
            for l in range(raio-1, len(imgY[0])-(raio-1)):
                #varre os indices da imagem ao redor do pixel de acordo com a mascara
                for c in range(i-(raio-1), i+(raio)):
                    for k in range(l-(raio-1), l+(raio)):
                        #aplica a mascara na banda Y
                        opY += (imgY[c][k][0] * mask[maskI][maskJ])
                        maskJ += 1
                    maskJ = 0
                    maskI += 1
                maskI = 0
                imgYAux[i][l][0] = opY
                
                #verificando os limites de RGB
                if (opY > 255):
                    imgYAux[i][l][0] = 255
                elif (opY < 0):
                    imgYAux[i][l][0] = 0
                    
                opY = 0
        return imgYAux
    
    #   Define uma mascara da media e usa convolucao com essa mascara
    def meanFilterRGB(self, img, m):
        mask = []
        for i in range(0, m):
            add = []
            for j in range(0, m):
                add.append(1/(m*m))
            mask.append(add)
        return self.convolutionRGB(img, mask)
    
    #   Define uma mascara da media e usa convolucao da banda Y com essa mascara
    def meanFilterY(self, img, m):
        mask = []
        for i in range(0, m):
            add = []
            for j in range(0, m):
                add.append(1/(m*m))
            mask.append(add)
        return self.yiqToRgb(self.convolutionY(img, mask))
    
    #   Define a mascara de sobel vertical e usa convolucao com essa mascara
    def sobelVerticalFilterRGB(self, img):
        mask = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
        return self.convolutionRGB(img, mask)
    
    #   Define a mascara de sobel vertical e usa convolucao com essa mascara
    def sobelVerticalFilterY(self, img):
        mask = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
        return self.convolutionY(img, mask)
    
    #   Define a mascara de sobel horizontal e usa convolucao com essa mascara
    def sobelHorizontalFilterRGB(self, img):
        mask = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
        return self.convolutionRGB(img, mask)
    
    #   Define a mascara de sobel horizontal e usa convolucao na banda Y com essa mascara
    def sobelHorizontalFilterY(self, img):
        mask = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
        return self.convolutionY(img, mask)
    
    #   Soma os operadores vertical e horizontal de Sobel resultando no filtro de Sobel
    def sobelFilterRGB(self, img):
        final = copy(img)
        vertical = self.sobelVerticalFilterRGB(img)
        horizontal = self.sobelHorizontalFilterRGB(img)
        
        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                final[i][l][0] = vertical[i][l][0] + horizontal[i][l][0]
                final[i][l][1] = vertical[i][l][1] + horizontal[i][l][1]
                final[i][l][2] = vertical[i][l][2] + horizontal[i][l][2]
                
                if (final[i][l][0] > 255):
                    final[i][l][0] = 255
                elif (final[i][l][0] < 0):
                    final[i][l][0] = 0
                    
                if (final[i][l][1] > 255):
                    final[i][l][1] = 255
                elif (final[i][l][1] < 0):
                    final[i][l][1] = 0
                    
                if (final[i][l][2] > 255):
                    final[i][l][2] = 255
                elif (final[i][l][2] < 0):
                    final[i][l][2] = 0
        return final
    
    #   Soma os operadores vertical e horizontal de Sobel aplicados na banda Y 
    #   resultando no filtro de Sobel
    def sobelFilterY(self, img):
        imgY = self.rgbToYiq(img)
        final = copy(imgY)
        vertical = self.sobelVerticalFilterY(img)
        horizontal = self.sobelHorizontalFilterY(img)
        
        for i in range(0, len(imgY)):
            for l in range(0, len(imgY[0])):
                final[i][l][0] = vertical[i][l][0] + horizontal[i][l][0]
                
                if (final[i][l][0] > 255):
                    final[i][l][0] = 255
                elif (final[i][l][0] < 0):
                    final[i][l][0] = 0
        return self.yiqToRgb(final)
####################################################################################
        
####################################################################################
######################## LIMIARIZACAO ##############################################
####################################################################################
    
    #   Limiariza uma imagem a partir de um "m" dado.    
    def limiarizationRGB(self, img, m):
        media = 0
        imgAux = copy(img)
        for i in range(0, len(img)):
            for l in range(0, len(img[0])):
                soma = int(img[i][l][0]) + int(img[i][l][1]) + int(img[i][l][2])
                media = soma/3
                if (media >= m):
                    imgAux[i][l][0] = 255
                    imgAux[i][l][1] = 255
                    imgAux[i][l][2] = 255
                else:
                    imgAux[i][l][0] = 0
                    imgAux[i][l][1] = 0
                    imgAux[i][l][2] = 0
                media = 0
        return imgAux
    
    #   Limiariza a banda Y a partir de um "m" dado
    def limiarizationY(self, img, m):
        imgY = self.rgbToYiq(img)
        imgYAux = copy(imgY)
        for i in range(0, len(imgY)):
            for l in range(0, len(imgY[0])):
                if (imgY[i][l][0] >= m):
                    imgYAux[i][l][0] = 255
                else:
                    imgYAux[i][l][0] = 0
        return self.yiqToRgb(imgYAux)
####################################################################################            
            
                    
