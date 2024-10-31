from abc import ABC, abstractmethod

class Jarat(ABC):

    def __init__(self):
        self.jaratszam= 0
        self.celallomas = ""
        self.jegyar = 0

    @property
    @abstractmethod
    def jaratszam(self):
            return  self.jaratszam

    @jaratszam.setter
    def jaratszam(self, jaratszam):
        self.jaratszam = jaratszam

    @property
    @abstractmethod
    def celallomas(self):
        return self.celallomas

    @celallomas.setter
    def celallomas(self, celallomas):
        self.celallomas = celallomas

    @property
    @abstractmethod
    def jegyar(self):
        return self.jegyar

    @jegyar.setter
    def jegyar(self, jegyar):
        self.jegyar = jegyar

