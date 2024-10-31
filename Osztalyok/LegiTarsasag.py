class Legitarsasag:
    def __init__(self):
        self._azonosito = 0
        self._nev = ""
        self._jarat = []

    @property
    def azonosito(self):
        return self._azonosito

    @azonosito.setter
    def azonosito(self, azonosito):
        self._azonosito = azonosito

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
        self._jarat.append(jarat)

