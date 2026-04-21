import numpy as np 

"""
Ce fichier s'occupe des différentes grilles du jeux. 
"""


#Classe case 

class Cases(): 
    
    def __init__(self, x, y): 
        self.x = x
        self.y = y 
        self.etat = "Vide" 
    

    



class GrilleJeu() : 

    def __init__(self, n_cases): 
        self.n_cases = n_cases 
        self.array = np.array([[None for i in range(n_cases)] for i in range(n_cases)]) 
        
