from Osztalyok.BelfoldiJarat import BelfoldiJarat
from Osztalyok.LegiTarsasag import Legitarsasag
from Osztalyok.NemzetkoziJarat import NemzetkoziJarat


def jegyFoglalas():
    pass

def foglalasLemondasa():
    pass

def foglalasokListazasa():
    pass



legitasasagok = []
belfoldijaratok = []
nemzetkozijaratok = []
foglalasok = []


def inicializacio():


    belfoldijarat1 = BelfoldiJarat()
    belfoldijarat1.jaratszam = 1
    belfoldijarat1.celallomas = "Debrecen"
    belfoldijarat1.jegyar = 12000

    legitasasag1 = Legitarsasag()
    legitasasag1.azonosito = 1
    legitasasag1.nev = "WizzAir"
    legitasasag1.jarat = "ABDC123"

    nemzetkozijarat1 = NemzetkoziJarat()
    nemzetkozijarat1.jaratszam = 1
    nemzetkozijarat1.celallomas = "Dubai"
    nemzetkozijarat1.jegyar = 150000

    nemzetkozijarat2 = NemzetkoziJarat()
    nemzetkozijarat2.jaratszam = 2
    nemzetkozijarat2.celallomas = "Barcelona"
    nemzetkozijarat2.jegyar = 45000

    legitasasagok.append(legitasasag1)
    belfoldijaratok.append(belfoldijarat1)
    nemzetkozijaratok.append(nemzetkozijarat1)
    nemzetkozijaratok.append(nemzetkozijarat2)
