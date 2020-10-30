import numpy as np
import cv2


def imagenGris(shape,image):

    matriz = np.zeros([shape[0],shape[1]])
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            val = image[f][c]
            total = sum(val)/3
            matriz[f][c] = total
    cv2.imwrite('Gris.jpg',matriz)
    return matriz
                                                                        

def imagenBN(mat):
    matrizbn = np.zeros([len(mat),len(mat[0])])
    for f in range(len(mat)):
        for c in range(len(mat[0])):
            v = mat[f][c]
            if v < 127.5:
                matrizbn[f][c] = 0
            else:
                matrizbn[f][c] = 255
    cv2.imwrite('BN.jpg',matrizbn)
    return matrizbn

def imagenConvPadd(mat,filtro):
    matriz_padd = np.zeros([len(mat)+2,len(mat[0])+2])
    tes = matriz_padd
    for f in range(len(mat)):
        for c in range(len(mat[0])):
            tes[f+1][c+1] = mat[f][c]
                                                                                                                                                                                                                                
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
    cv2.imwrite('Imagen_Convolucion_Con_Padding.jpg',matriz_padd)
    return matriz_padd

def imagenconv(mat,filtro):
    resultado = np.zeros([len(mat)-2,len(mat[0])-2])
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
    cv2.imwrite('Imagen_Convolucion_Sin_Padding.jpg',resultado)
    return resultado 


fil = [[1,1,1],[1,0,1],[1,1,1]]

imagen = cv2.imread('lego.png')
img = imagen.shape
gris = imagenGris(img,imagen)
bn = imagenBN(gris)
conv_padd = imagenConvPadd(gris, fil)
conv = imagenconv(gris, fil)

