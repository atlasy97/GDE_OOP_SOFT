from Osztalyok.BelfoldiJarat import BelfoldiJarat
from Osztalyok.JegyFoglalas import Jegyfoglalas
from Osztalyok.LegiTarsasag import Legitarsasag
from Osztalyok.NemzetkoziJarat import NemzetkoziJarat


def jegyFoglalas(foglalandoJarat:str) -> bool :
    sikeres = False


    return sikeres

def foglalasLemondasa(lemondado:str, szin) -> bool :
    sikeres = False

    try:
        id = int(lemondado)
        for elem in foglalasok:
            if elem.azonosito == id:
                print(szin.Alahuzas + szin.Zold + "FOGLALÁS SIKERESEN TÖRÖLVE:"  + szin.Zaras + "| ID:" + str(elem.azonosito)+ " | NÉV: " + str(elem.nev) + " | JÁRATSZÁM:" + str(elem.jarat.jaratszam))
                foglalasok.remove(elem)
                sikeres = True
                break
        if sikeres == False:
            print(szin.Sarga+"NINCS ILYEN ID, ÍGY NEM LETT FOGLALÁS LEMONDVA" + szin.Zaras)
    except:
        print("Ez nem egy egészszám, az ID csak egész szám lehet")
    return sikeres

def foglalasokListazasa(szin):
    for foglalas in foglalasok:
        print(szin.Felkover + szin.Kek +str(foglalas.azonosito) +"   "+ str(foglalas.jarat.jaratszam)+ "   "  + foglalas.nev  + szin.Zaras)




legitarsasagok = []
foglalasok = []


def inicializacio():

    belfoldijarat1 = BelfoldiJarat()
    belfoldijarat1.jaratszam = "W62441"
    belfoldijarat1.celallomas = "Debrecen"
    belfoldijarat1.jegyar = 12000


    nemzetkozijarat1 = NemzetkoziJarat()
    nemzetkozijarat1.jaratszam = "W54441"
    nemzetkozijarat1.celallomas = "Dubai"
    nemzetkozijarat1.jegyar = 150000

    nemzetkozijarat2 = NemzetkoziJarat()
    nemzetkozijarat2.jaratszam = "W13541"
    nemzetkozijarat2.celallomas = "Barcelona"
    nemzetkozijarat2.jegyar = 45000

    legitarsasag1 = Legitarsasag()
    legitarsasag1.azonosito = 1
    legitarsasag1.nev = "WizzAir"
    legitarsasag1.jarat = [belfoldijarat1, nemzetkozijarat1, nemzetkozijarat2]


    legitarsasagok.append(legitarsasag1)



    foglalas1 = Jegyfoglalas()
    foglalas1.jarat = belfoldijarat1
    foglalas1.nev = "Kiss István"

    foglalas2 = Jegyfoglalas()
    foglalas2.jarat = belfoldijarat1
    foglalas2.nev = "Gábor István"

    foglalas3 = Jegyfoglalas()
    foglalas3.jarat = nemzetkozijarat1
    foglalas3.nev = "Ferenczi József"

    foglalas4 = Jegyfoglalas()
    foglalas4.jarat = nemzetkozijarat1
    foglalas4.nev = "Minta Béla"

    foglalas5 = Jegyfoglalas()
    foglalas5.jarat = nemzetkozijarat2
    foglalas5.nev = "Szekér Boglárka"

    foglalas6 = Jegyfoglalas()
    foglalas6.jarat = nemzetkozijarat1
    foglalas6.nev = "Kovács Irén"

    foglalasok.append(foglalas1)
    foglalasok.append(foglalas2)
    foglalasok.append(foglalas3)
    foglalasok.append(foglalas4)
    foglalasok.append(foglalas5)
    foglalasok.append(foglalas6)