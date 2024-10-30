#KÉPERNYŐK
from Osztalyok.BelfoldiJarat import BelfoldiJarat


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


    print(r"Üssön 0-t (nulla) a kezdőképernyőhöz történő visszatéréshez")



def lemondasKepernyo():
    print(szin.Felkover + szin.Sarga +r"       __|__" + szin.Zaras)
    print(szin.Felkover + szin.Sarga +r"--o--o--(_)--o--o--" + szin.Zaras)
    print(szin.Felkover + szin.Sarga + szin.Alahuzas + " FOGLALÁS LEMONDÁSA " + szin.Zaras)
    print(r"Üssön 0-t (nulla) a kezdőképernyőhöz történő visszatéréshez")



def listazasKepernyo():
    print(szin.Felkover + szin.Kek +r"                  / \ " + "                     PILLANATNYI FOGLALÁSOK LISTÁJA" + szin.Zaras)
    print(szin.Felkover + szin.Kek +r"                 |^^|" + "" + szin.Zaras)
    print(szin.Felkover + szin.Kek +r"                 |{}|" + "" + szin.Zaras)
    print(szin.Felkover + szin.Kek +r"  _______________/~~\________________" + "" + szin.Zaras)
    print(szin.Felkover + szin.Kek +r" /               |  |                \ " + "" + szin.Zaras)
    print(szin.Felkover + szin.Kek +r"`========--------.  .---------========'" + "" + szin.Zaras)
    print(szin.Felkover + szin.Kek +r"                 ||||" + "" + szin.Zaras)
    print(szin.Felkover + szin.Kek +r"                  ||" + "" + szin.Zaras)
    print(szin.Felkover + szin.Kek +r"                  ||" + "" + szin.Zaras)
    print(szin.Felkover + szin.Kek +r"                  ||" + "" + szin.Zaras)
    print(szin.Felkover + szin.Kek +r"                  ||" + "" + szin.Zaras)
    print(szin.Felkover + szin.Kek +r"              ,---||---," + "" + szin.Zaras)
    print(szin.Felkover + szin.Kek +r"              '---<>---'" + "" + szin.Zaras)
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
    Kek = '\033[94m'
    Turkiz = '\033[96m'
    Zold = '\033[92m'
    Sarga = '\033[93m'
    Piros = '\033[91m'
    Felkover = '\033[1m'
    Alahuzas = '\033[4m'
    Zaras = '\033[0m'