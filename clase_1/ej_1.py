import numpy as np

#norma0 
def vector_norm_l0(m):
    mascara = m > 0
    return np.sum(mascara,axis=1)

def vector_norm_l1(m):
    vector_abs = np.absolute(m)
    vector_suma = np.sum(vector_abs,axis=1)
    return vector_suma

#norma2
def vector_norm_l2(m):
    vector_cuadrado = np.power(m,2)
    sumas_de_cuadrados_de_vector = np.sum(vector_cuadrado,axis=1)
    raiz_de_las_sumas = np.sqrt(sumas_de_cuadrados_de_vector)
    return raiz_de_las_sumas

#norma infinito
def vector_norm_inf(m):
    matrix_abs_mayor = np.amax(m,axis=1)
    return matrix_abs_mayor


#lo vector = np.array([[1,0,3,0],[1,2,0,4]])
# vector m vector = np.array([[1,-2,3,-4],[1,2,-2,4]])
#vector norma2 vector = np.array([[1,2,3,4],[1,2,-2,4]])
#matrix = np.array([[-9,-1,3,4],[1,2,-2,4]])