from abc import ABC, abstractmethod
import random


class Carte(ABC):

    def __init__(self):
        self.visuel = None
        self.nom = None


class CartePassive(Carte, ABC):

    def __init__(self):
        super().__init__()


class CarteActive(Carte, ABC):

    def __init__(self):
        super().__init__()
