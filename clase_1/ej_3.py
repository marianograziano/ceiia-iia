import numpy as np

#def id2idx(entero):
#    ids = np.array([15,12,14,10,1,2,1,14,12,10,9])
#    elementos_unicos = np.unique(a,return_index=True)
    
    

id_usuarios= np.array([15,12,14,10,1,2,1])
esperado = np.arrapy([0,1,2,3,4,5,4])

unicos, indices_ind, indices_inv = np.unique(id_usuarios,return_index=True,return_inverse=True)
print(esperado)
print(f'El vector original {id_usuarios}')
print(f'El vector esperado {esperado}')
print(f'Los elementos unicos del vector original {unicos}')
print(f'Indice de elementos {indices_ind}')
print(f'Indice de elementos -1 {indices_ind *-1}')
print(f'Indice de elementos inv {indices_inv}')
print(f'Indice de elementos inv -1  {indices_inv * -1}')


#_print(unicos[indices])
#indice_a_buscar = 9
#id_a_buscar = 14
#print(unicos[indices][indice_a_buscar])