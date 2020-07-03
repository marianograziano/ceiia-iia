import pickle
import numpy as np

class Analisis_Ratings:
    instance = None
    archivo_pik = None
    def __new__(cls,archivo):
        
        if Analisis_Ratings.instance is None:
            Analisis_Ratings.instance = super(Analisis_Ratings, cls).__new__(cls)
            return Analisis_Ratings.instance
        else:
            return Analisis_Ratings.instance
    def __init__(self,archivo):
        
        self.archivo = archivo
        tipos = [('userId', (np.int16)), ('movieId', (np.int32)), ('rating', (np.float16)), ('timestamp', (np.int64))] 
        ratings = np.genfromtxt(self.archivo, delimiter = ',',dtype = tipos) 
        try:
            ratings_levantado = pickle.load(open("dataset.pki", "rb"))
            #print('Se encontro el archivo')
        except (OSError, IOError) as e:
            #print('No se encontro el archivo')
            ratings_levantado = pickle.dump(ratings, open("dataset.pki", "wb"),protocol=pickle.HIGHEST_PROTOCOL)
        
Analisis =  Analisis_Ratings('ratings-short.csv')
Analisis1 =  Analisis_Ratings('ratings-short1.csv')
print(hex(id(Analisis)))
print(hex(id(Analisis1)))