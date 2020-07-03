import numpy as np 
from ej_1 import vector_norm_l2

def orden_segun_l2(m):
    l2 = vector_norm_l2(m)
    l2_argsort = np.argsort(l2)
    l2_argsort_may = m[l2_argsort[::-1]]
    return l2_argsort_may

def sorting_vectors_by_norm_l2(matrix):
    norm_l2 = vector_norm_l2(matrix)
    arg_sort = np.argsort(norm_l2 * -1)
    return matrix[arg_sort, :]



