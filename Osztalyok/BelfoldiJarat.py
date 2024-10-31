from Osztalyok.Jarat import Jarat


class BelfoldiJarat(Jarat):
    def __init__(self):
        self._jaratszam = 0
        self._celallomas = ""
        self._jegyar = 0


    @property
    def jaratszam(self):
            return  self._jaratszam

    @jaratszam.setter
    def jaratszam(self, jaratszam):
        self._jaratszam = jaratszam

    @property
    def celallomas(self):
        return self._celallomas

    @celallomas.setter
    def celallomas(self, celallomas):
        self._celallomas = celallomas

    @property
    def jegyar(self):
        return self._jegyar

    @jegyar.setter
    def jegyar(self, jegyar):
        self._jegyar = jegyar
