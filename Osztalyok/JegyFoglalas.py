from Osztalyok.Jarat import Jarat

_foglalasszamlalo = 0

def foglalasszamlalo_lekeres():
    return  _foglalasszamlalo

def ujfoglalas()->int:
    global _foglalasszamlalo
    _foglalasszamlalo = foglalasszamlalo_lekeres()+1
    return _foglalasszamlalo

class Jegyfoglalas:


    def __init__(self):
        self._azonosito = ujfoglalas()
        self._nev = ""
        self._jarat = 0

    @property
    def azonosito(self):
        return self._azonosito

    @azonosito.setter
    def azonosito(self):
        self._azonosito = ujfoglalas()

    @property
    def nev(self):
        return self._nev

    @nev.setter
    def nev(self, nev):
        self._nev = nev

    @property
    def jarat(self):
        return self._jarat

    @jarat.setter
    def jarat(self, jarat):
        self._jarat = jarat
