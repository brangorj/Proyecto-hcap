import numpy as np
import cv2


def imagenGris(shape,image):
#se crea la matriz de zeros
    matriz = np.zeros([shape[0],shape[1]])
#Interaccion por cada elemento de los datos de la imagen para hacerla en escala de grises
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            val = image[f][c]
            total = sum(val)/3
            matriz[f][c] = total
#Crea la imagen en escala de grises
    cv2.imwrite('Gris.jpg',matriz)
#Regresa la matriz resultante
    return matriz
                                                                        

def imagenBN(mat):
#Crea la matriz de zeros
    matrizbn = np.zeros([len(mat),len(mat[0])])
#Revisa cada elemento y lo pasa a valores ded 0 o 255
    for f in range(len(mat)):
        for c in range(len(mat[0])):
            v = mat[f][c]
            if v < 127.5:
                matrizbn[f][c] = 0
            else:
                matrizbn[f][c] = 255
#Crea la imagen en blanco y negro
    cv2.imwrite('BN.jpg',matrizbn)
#Regresa la matriz de valores en blanco y negro
    return matrizbn

def imagenConvPadd(mat,filtro):
    #Se crea la matriz de 0
    matriz_padd = np.zeros([len(mat)+2,len(mat[0])+2])
    tes = matriz_padd
    #Con la copia de la matriz de 0 se empiezan a meter los datos de la imagen para que tenga su
    #marco de 0
    for f in range(len(mat)):
        for c in range(len(mat[0])):
            tes[f+1][c+1] = mat[f][c]
    
    #Se hace la convolucion
    for f in range(len(mat)-2):
        for c in range(len(mat[0])-2):
            val1 = (tes[f][c]*filtro[0][0])+(tes[f][c+1]*filtro[0][1])+(tes[f][c+2]*filtro[0][2])
            val2 = (tes[f+1][c]*filtro[1][0])+(tes[f+1][c+1]*filtro[1][1])+(tes[f+1][c+2]*filtro[1][2])
            val3 = (tes[f+2][c]*filtro[2][0])+(tes[f+2][c+1]*filtro[2][1])+(tes[f+2][c+2]*filtro[2][2])
            suma = val1 + val2 + val3
            if suma >= 255:
                matriz_padd[f][c] = 255
            else:    
                matriz_padd[f][c] = suma
    #Se crea la imagen con convolucion y padding
    cv2.imwrite('Imagen_Convolucion_Con_Padding.jpg',matriz_padd)
    #Regresa la matriz resultante
    return matriz_padd

def imagenconv(mat,filtro):
    #Se crea la matriz de 0
    resultado = np.zeros([len(mat)-2,len(mat[0])-2])
    #Se hace la convolucion
    for f in range(len(resultado)):
        for c in range(len(resultado[0])):
            val1 = (mat[f][c]*filtro[0][0])+(mat[f][c+1]*filtro[0][1])+(mat[f][c+2]*filtro[0][2])
            val2 = (mat[f+1][c]*filtro[1][0])+(mat[f+1][c+1]*filtro[1][1])+(mat[f+1][c+2]*filtro[1][2])
            val3 = (mat[f+2][c]*filtro[2][0])+(mat[f+2][c+1]*filtro[2][1])+(mat[f+2][c+2]*filtro[2][2])
            suma = val1 + val2 + val3
            if suma >= 255:
                resultado[f][c] = 255
            else:    
                resultado[f][c] = suma
    #Se crea la imagen con convolucion
    cv2.imwrite('Imagen_Convolucion_Sin_Padding.jpg',resultado)
    #Regresa la matriz con convolucion
    return resultado 

#Filtro que se va a aplicar
fil = [[1,1,1],[1,0,1],[1,1,1]]
#Imagen a procesar
imagen = cv2.imread('lego.png')
#Tamaño de la imagen
img = imagen.shape
#Matriz en escala de grises
gris = imagenGris(img,imagen)
#Matriz en blanco y negro
bn = imagenBN(gris)
#Matriz con convolucion y pading
conv_padd = imagenConvPadd(gris, fil)
#Matriz con convolucion
conv = imagenconv(gris, fil)

