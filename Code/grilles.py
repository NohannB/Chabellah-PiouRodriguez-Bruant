import numpy as np
import random

"""
Ce fichier s'occupe des différentes grilles du jeux. 
"""


# Classe case

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

# Polyomino


class GrilleJeu():

    def __init__(self, n_cases=10):
        self.n_cases = n_cases
        self.array = np.array(
            [[Case(x, y) for y in range(n_cases)] for x in range(n_cases)])

    def __getitem__(self, key):
        return self.array[key[0], key[1]]


class Polyomino():
    ListFormes = []
    ListFormes.append(np.array([[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]]))
    ListFormes.append(np.array([[1, 1],
                                [1, 1],]))
    ListFormes.append(np.array([[1]],))
    ListFormes.append(np.array([[1, 1, 1, 1]],))
    ListFormes.append(np.array([[1, 0],
                                [1, 0],
                                [1, 1]]))
    ListFormes.append(np.array([[0, 1, 1],
                                [1, 1, 0]]))

    ListCouleurs = ['corail', 'poisson', 'crustace',
                    'pollution', 'toto', 'chalutier']

    ListPoidsCouleurs = [22, 22, 22, 12, 12, 10]
    ListPoidsFormes = [10, 20, 10, 20, 20, 20]

    def __init__(self):
        # Création de forme et couleur aléatoire
        self.array = random.choices(
            Polyomino.ListFormes, weights=Polyomino.ListPoidsFormes, k=1)[0]
        self.couleur = random.choices(
            Polyomino.ListCouleurs, weights=Polyomino.ListPoidsCouleurs, k=1)[0]

        # Position de base dans la grille
        self.x = 0
        self.y = 0

        # Rotation aléatoire de la forme
        for i in range(random.randint(0, 3)):
            self.rotation()
            for i in range(random.randint(0, 1)):
                self.symetrie()

    def rotation(self):
        l, c = self.array.shape
        new = np.zeros((c, l))
        for i in range(c):
            new[i, :] = self.array[:, i].T
        self.array = new
        self.symetrie()

    def symetrie(self):
        l = self.array.shape[0]
        new = np.zeros(self.array.shape)
        for i in range(l):
            new[i, :] = self.array[i, ::-1]
        self.array = new

    def translate(self, dx, dy, ngrid):
        assert self.x+dx + \
            self.array.shape[0] < ngrid and self.y + \
            dy+self.array.shape[1] < ngrid
        self.x += dx
        self.y += dy

    def modifierPolyo(self):
        self.array = random.choices(
            Polyomino.ListFormes, weights=Polyomino.ListPoidsFormes, k=1)[0]
        self.couleur = random.choices(
            Polyomino.ListCouleurs, weights=Polyomino.ListPoidsCouleurs, k=1)[0]

        for i in range(random.randint(0, 3)):
            self.rotation()
            for i in range(random.randint(0, 1)):
                self.symetrie()

    def __str__(self):
        s = self.array.shape
        c = ""
        for i in range(s[0]):
            for j in range(s[1]):
                if self.array[i, j]:
                    c += 'x'
                else:
                    c += " "
            c += "\n"
        return c


if __name__ == "__main__":
    grille = GrilleJeu()
    print(grille[2, 2].getEtat())

    grille[2, 2].changeEtat("Corrail")
    print(grille[2, 2].getEtat())

    # tab = np.array([[1, 0, 0], [1, 1, 1]])
    p = Polyomino()
    print(p.couleur)
    print(p)
    p.rotation()
    print(p)
