import numpy as np 

"""
Ce fichier s'occupe des différentes grilles du jeux. 
"""


#Classe case 

class Case(): 
    
    def __init__(self, x, y):
        """
        Entrée :  
            - x : int 
                Ligne de la case crée 
            -y : int 
                Colone de la case crée
        Sortie : 
            Nouvelle case
        """
        self.__x = x
        self.__y = y 
        self.__etat = "Vide"
    
    def changeEtat(self, nouvelEtat):
        """
        Change l'état d'une case
        Entrée : 
            - nouvelEtat : string 
                Nouvel état de la case
        Sortie : 
            None 
        """
        self.__etat = nouvelEtat 
    
    def getEtat(self): 
        """
        Récupère et renvoie l'état d'une case. 
        Entrée : 
            None
        Sortie : 
            String 
                Etat de la case
        """
        return self.__etat
  
#Polyomino 


class GrilleJeu() : 

    def __init__(self, n_cases = 10): 
        self.n_cases = n_cases 
        self.array = np.array([[Case(x,y) for y in range(n_cases)] for x in range(n_cases)]) 
    
    def __getitem__(self, key):
        return self.array[key[0],key[1]] 
    


class Polyomino() : 

    def __init__(self, tab, couleur) :
        self.array = tab 
        self.couleur = couleur 
        self.x = 0 
        self.y = 0 
    
    def rotation(self) : 
        l,c = self.array.shape 
        new = np.zeros((c,l))
        for i in range(c) : 
            new[l-i,:] = self.array[:,i].T
        self.array = new
    
    def symetrie(self) : 
        l = self.array.shape[0] 
        new = np.zeros(self.array.shape)
        for i in range(l) : 
            new[i,:] = self.array[i,::-1]
        self.array = new
    
    def translate(self, dx, dy, ngrid) :
        assert sefl.x+dx+ self.array.shape[0] and self.y+dy+self.array.shape[1] 
        self.x+=dx
        self.y+=dy 
         

        


    def __str__(self) : 
        s = self.array.shape
        c = ""
        for i in range(s[0]) : 
            for j in range(s[1]) : 
                if self.array[i,j] : 
                    c+= self.couleur
                else : 
                    c+= " "
            c+="\n"
        return c




if __name__ == "__main__" : 
    grille = GrilleJeu() 
    print(grille[2,2].getEtat())

    grille[2,2].changeEtat("Corrail")
    print(grille[2,2].getEtat())
        

    tab = np.array([[1,0,0],[1,1,1]])
    p = Polyomino(tab,'r') 

    print(p)
    p.rotation() 
    print(p)

    p.symetrie()
    print(p)
