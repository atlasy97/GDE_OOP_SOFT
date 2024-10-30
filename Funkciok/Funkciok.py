import Osztalyok
from Funkciok.Kepernyok import *


def jegyFoglalas():
    pass

def foglalasLemondasa():
    pass

def foglalasokListazasa():
    pass



def bemenetFeldolgozas():
    valasztottFunckio = input()
    kepernyoTisztitas()
    if valasztottFunckio.lower().strip() == "1":
        print("Okej! (1)")
    elif valasztottFunckio.lower().strip() == "2":
        print("Okej! (2)")
    elif valasztottFunckio.lower().strip() == "3":
        listazasKepernyo()
    elif valasztottFunckio.lower().strip() == "0":
        kezdoKepernyo()


def kepernyoTisztitas():
    tolas = "\n" * 100
    print(tolas)