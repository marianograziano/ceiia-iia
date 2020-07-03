import numpy as np

#norma0 
def norma_lo(m):
    mascara = m > 0
    return np.sum(mascara)

def norma_l1(m):
    vector_abs = np.absolute(m)
    vector_suma = vector_abs.sum()
    return vector_suma

#norma2
def norma_l2(m):
    vector_cuadrado = np.power(m,2)
    sumas_de_cuadrados_de_vector = float(vector_cuadrado.sum())
    raiz_de_las_sumas = np.sqrt(sumas_de_cuadrados_de_vector)
    return raiz_de_las_sumas

#norma infinito
def norma_li(m):
    matrix_abs = np.absolute(m)
    matrix_abs_mayor = np.ndarray.max(matrix_abs)
    return matrix_abs_mayor

matr = np.array([[1,0,3,0],[1,2,0,4]])
print(norma_lo(matr))
#lo vector = np.array([[1,0,3,0],[1,2,0,4]])
# vector m vector = np.array([[1,-2,3,-4],[1,2,-2,4]])
#vector norma2 vector = np.array([[1,2,3,4],[1,2,-2,4]])
#matrix = np.array([[-9,-1,3,4],[1,2,-2,4]])