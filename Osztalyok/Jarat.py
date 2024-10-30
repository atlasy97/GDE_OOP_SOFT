from abc import ABC, abstractmethod

class Jarat(ABC):
    @property
    @abstractmethod
    def jaratszam(self):
            pass

    @property
    @abstractmethod
    def celallomas(self):
        pass

    @property
    @abstractmethod
    def jegyar(self):
        pass

    @abstractmethod
    def kiiratas(self):
        pass

