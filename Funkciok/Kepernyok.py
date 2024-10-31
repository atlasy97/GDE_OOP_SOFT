#KÉPERNYŐK
from Funkciok.Funkciok import jegyFoglalas, legitarsasagok, legitarsasagok, foglalasok
from Osztalyok.BelfoldiJarat import BelfoldiJarat
from Osztalyok.NemzetkoziJarat import NemzetkoziJarat


def kezdoKepernyo():
    print(szin.Felkover + szin.Piros +r"            ______"+ szin.Zaras)
    print(szin.Felkover + szin.Piros +r"            _\ _~-\___"+ szin.Zaras)
    print(szin.Felkover + szin.Piros +r"    =  = ==(____AA____D"+ szin.Zaras)
    print(szin.Felkover + szin.Piros +r"                \_____\___________________,-~~~~~~~`-.._"+ szin.Zaras)
    print(szin.Felkover + szin.Piros +r"                /     o O o o o o O O o o o o o o O o  |\_"+ szin.Zaras)
    print(szin.Felkover + szin.Piros +r"                `~-.__        ___..----..                  )"+ szin.Zaras)
    print(szin.Felkover + szin.Piros +r"                      `---~~\___________/------------`````"+ szin.Zaras)
    print(szin.Felkover + szin.Piros +r"                      =  ===(_________D"+ szin.Zaras)
    print(szin.Felkover + szin.Piros +r"           PARAIZS ATTILA XT121U Repülőjegy Foglalási Rendszer" + szin.Zaras)
    print(szin.Piros + "Funkciók:" + szin.Alahuzas + szin.Zaras)
    print(szin.Alahuzas +   szin.Turkiz + "-|- 1) Jegy foglalása -|-" + szin.Zaras +"   " + szin.Alahuzas + szin.Sarga + " -|- 2) Foglalás lemondása -|-" + szin.Zaras +"   "  + szin.Alahuzas + szin.Kek +  "-|- 3) foglalások listázása -|-" + szin.Zaras)
    print("Üsse be a használni kívánt funkció számát: ")

def jegyFoglalasKepernyo():
    print(szin.Felkover + szin.Turkiz +r"           _"+ szin.Zaras)
    print(szin.Felkover + szin.Turkiz +r"         -=\`\ "+ szin.Zaras)
    print(szin.Felkover + szin.Turkiz +r"     |\ ____\_\__"+ szin.Zaras)
    print(szin.Felkover + szin.Turkiz +r"   -=\c```````` ``)"+ szin.Zaras)
    print(szin.Felkover + szin.Turkiz +r"      `~~~~~/ /~~`"+ szin.Zaras)
    print(szin.Felkover + szin.Turkiz +r"        -==/ /"+ szin.Zaras)
    print(szin.Felkover + szin.Turkiz +r"          '-'"+ szin.Zaras)
    print(szin.Felkover + szin.Turkiz + szin.Alahuzas + "      JEGY FOGLALÁSA      " + szin.Zaras)

    print(szin.Fekete + szin.PirosHatter+"Belfö" + szin.Zaras + szin.Fekete +  szin.FeherHatter + "ldi já" + szin.Zaras + szin.ZoldHatter +szin.Fekete +  "ratok:" + szin.Zaras)

    for legitarsasag in legitarsasagok:
        for bjar in legitarsasag.jarat:
            for jar in bjar:
                if type(jar) is BelfoldiJarat:
                    print("|Járatazonosító: ",jar.jaratszam,"| Légitársaság: ", legitarsasag.nev , "| Célállomás: ", jar.celallomas , "| Jegyár: ",jar.jegyar,"Ft |")

    print(szin.Fekete +szin.SargaHatter +"Nemzetközi járatok:" + szin.Zaras)

    for legitarsasag in legitarsasagok:
        for kjar in legitarsasag.jarat:
            for jar in kjar:
                if type(jar) is NemzetkoziJarat:
                    print("|Járatazonosító: ", jar.jaratszam, "| Légitársaság: ", legitarsasag.nev, "| Célállomás: ", jar.celallomas, "| Jegyár: ", jar.jegyar, "Ft |")

    print("Üssön 0-t (nulla) a kezdőképernyőhöz történő visszatéréshez, vagy a járatszámot a foglaláshoz")

    leutottBillentyu = "x"
    while (leutottBillentyu != "0"):
        leutottBillentyu = input()
        if(leutottBillentyu != "0"):
          jegyFoglalas(leutottBillentyu)
        else:
            kepernyoTisztitas()
            kezdoKepernyo()


def lemondasKepernyo():
    print(szin.Felkover + szin.Sarga +r"       __|__" + szin.Zaras)
    print(szin.Felkover + szin.Sarga +r"--o--o--(_)--o--o--" + szin.Zaras)
    print(szin.Felkover + szin.Sarga + szin.Alahuzas + " FOGLALÁS LEMONDÁSA " + szin.Zaras)
    print(r"Üssön 0-t (nulla) a kezdőképernyőhöz történő visszatéréshez")



def listazasKepernyo():
    print(szin.Felkover + szin.Kek +r"  __" + szin.Zaras)
    print(szin.Felkover + szin.Kek +r"  \  \     _ _" + szin.Zaras)
    print(szin.Felkover + szin.Kek +r"   \**\ ___\/ \ " + szin.Zaras)
    print(szin.Felkover + szin.Kek +r"X*#####*+^^ \_ \ " + szin.Zaras)
    print(szin.Felkover + szin.Kek +r"   o/\  \ " + szin.Zaras)
    print(szin.Felkover + szin.Kek +r"      \__\ " + szin.Zaras)
    print(szin.Felkover + szin.Kek +r"PILLANATNYI FOGLALÁSOK LISTÁJA" + szin.Zaras)
    print(szin.Felkover + szin.Kek +r"ID---JÁRAT---FOGLALÓ NEVE"  + szin.Zaras)

    for foglalas in foglalasok:
        print(szin.Felkover + szin.Kek +str(foglalas.azonosito) +"   "+ str(foglalas.jarat.jaratszam)+ "   "  + foglalas.nev  + szin.Zaras)

    print(r"Üssön 0-t (nulla) a kezdőképernyőhöz történő visszatéréshez")


def hibaKepernyo(kepernyo: int):
    if(kepernyo == 0):
        kezdoKepernyo()
    elif(kepernyo == 1):
        jegyFoglalasKepernyo()
    elif(kepernyo == 2):
        lemondasKepernyo()
    elif(kepernyo == 3):
        listazasKepernyo()
    print(
        szin.Alahuzas + szin.Turkiz + "-|- 1) Jegy foglalása -|-" + szin.Zaras + "   " + szin.Alahuzas + szin.Sarga + " -|- 2) Foglalás lemondása -|-" + szin.Zaras + "   " + szin.Alahuzas + szin.Kek + "-|- 3) foglalások listázása -|-" + szin.Zaras)
    print(szin.Felkover + szin.Piros +"A beadott érték nem értelmezhető kérem csak a megadottak közül válasszon" + szin.Zaras)

#KIEGÉSZÍTŐ FUNKCIÓK, OSZTÁLYOK, VÁLTOZÓK

kepernyo: int = 0
def bemenetFeldolgozas():
    valasztottFunckio = input()
    try:
        global kepernyo
        kepernyo = int(valasztottFunckio.lower().strip())
    except:
        hibaKepernyo(0)
    kepernyoTisztitas()
    if valasztottFunckio.lower().strip() == "0":
        kezdoKepernyo()
    elif valasztottFunckio.lower().strip() == "1":
        jegyFoglalasKepernyo()
    elif valasztottFunckio.lower().strip() == "2":
        lemondasKepernyo()
    elif valasztottFunckio.lower().strip() == "3":
        listazasKepernyo()
    else:
        hibaKepernyo(kepernyo)

def kepernyoTisztitas():
    tolas = "\n" * 100
    print(tolas)

class szin:
    Fekete = '\33[30m'
    FeherHatter ='\33[107m'
    Kek = '\033[94m'
    Turkiz = '\033[96m'
    Zold = '\033[92m'
    ZoldHatter = '\33[42m'
    Sarga = '\033[93m'
    SargaHatter = '\33[43m'
    Piros = '\033[91m'
    PirosHatter ='\33[41m'
    Felkover = '\033[1m'
    Alahuzas = '\033[4m'
    Zaras = '\033[0m'

def megjelenitesiNevLekerese(nev:str) ->str:
    if nev== "_jaratszam":
        return  "Járatszám:"
    elif nev== "_celallomas":
        return "Célállomás:"
    elif nev== "_jegyar":
        return  "Jegyár:"
