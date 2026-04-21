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
        self.cooldown = None
        self.count_cooldown = None

    def activation_carte(self):
        pass


class CarteSymetrie(Carte):

    def __init__(self):
        super().__init__()
        self.cooldown = None
        self.count_cooldown = None

    def activation_carte(self):
        pass


class CarteChangerPolyomino(Carte):

    def __init__(self):
        super().__init__()
        self.cooldown = 2
        self.count_cooldown = 0

    def activation_carte(self):
        pass


class CarteLibererCasePolluee(Carte):

    def __init__(self):
        super().__init__()
        self.cooldown = 3
        self.count_cooldown = 0

    def activation_carte(self):
        pass


class CarteVoirPolyominoSuivant(Carte):

    def __init__(self):
        super().__init__()
        self.cooldown = 2
        self.count_cooldown = 0

    def activation_carte(self):
        pass
