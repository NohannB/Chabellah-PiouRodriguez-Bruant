from abc import ABC, abstractmethod
import random

# Classe abstraite générale


class Carte(ABC):

    def __init__(self):
        self.visuel = None
        self.nom = None

    @abstractmethod
    def activation_carte(self):
        pass


# Cartes actives
class CarteTourner(Carte):

    def __init__(self):
        super().__init__()
        self.cooldown = 0
        self.count_cooldown = 0

    def activation_carte(self, polyo):
        polyo.rotation()


class CarteSymetrie(Carte):

    def __init__(self):
        super().__init__()
        self.cooldown = 0
        self.count_cooldown = 0

    def activation_carte(self, polyo):
        polyo.symetrie()


class CarteChangerPolyomino(Carte):

    def __init__(self):
        super().__init__()
        self.cooldown = 2
        self.count_cooldown = 0

    def activation_carte(self, polyo):
        polyo.modifierPolyo()


class CarteLibererCasePolluee(Carte):

    def __init__(self):
        super().__init__()
        self.cooldown = 3
        self.count_cooldown = 0

    def activation_carte(self, grille, posx, posy):
        pass


class CarteVoirPolyominoSuivant(Carte):

    def __init__(self):
        super().__init__()
        self.cooldown = 2
        self.count_cooldown = 0

    def activation_carte(self):
        pass


# Cartes Passives
class CarteAugmenterScore(Carte):

    def activation_carte(self, partie):
        partie.score += 20


class CarteBoostCouleur(Carte):

    def activation_carte(self):
        pass


class CarteAugmenterTauxCouleur(Carte):

    def activation_carte(self):
        pass
