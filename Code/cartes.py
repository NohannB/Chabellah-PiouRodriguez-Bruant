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

    def modifier_cooldown(self):
        pass


class CarteSymetrie(Carte):

    def __init__(self):
        super().__init__()
        self.cooldown = 0
        self.count_cooldown = 0

    def activation_carte(self, polyo):
        polyo.symetrie()

    def modifier_cooldown(self):
        pass


class CarteChangerPolyomino(Carte):

    def __init__(self):
        super().__init__()
        self.cooldown = 2
        self.count_cooldown = 0

    def activation_carte(self, polyo):
        if self.count_cooldown == 0:
            polyo.modifierPolyo()
            self.count_cooldown = 3

    def modifier_cooldown(self):
        if self.cooldown > 0:
            self.cooldown -= 1


class CarteLibererCasePolluee(Carte):

    def __init__(self):
        super().__init__()
        self.cooldown = 3
        self.count_cooldown = 0

    def activation_carte(self, grille, posx, posy):
        pass

    def modifier_cooldown(self):
        pass


class CarteVoirPolyominoSuivant(Carte):

    def __init__(self):
        super().__init__()
        self.cooldown = 2
        self.count_cooldown = 0

    def activation_carte(self):
        pass

    def modifier_cooldown(self):
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
