from Funkciok import Funkciok


class szin:
    Kek = '\033[94m'
    Turkiz = '\033[96m'
    Zold = '\033[92m'
    Sarga = '\033[93m'
    Piros = '\033[91m'
    Felkover = '\033[1m'
    Alahuzas = '\033[4m'
    Zaras = '\033[0m'

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
    print("A súgó használatához üssön ? (kérdőjelet) majd nyomja meg az ENTER billentyűt")
    print(szin.Piros + "Funkciók:" + szin.Alahuzas + szin.Zaras)
    print(szin.Alahuzas +   szin.Turkiz + "-|- 1) Jegy foglalása -|-" + szin.Zaras +"   " + szin.Alahuzas + szin.Sarga + " -|- 2) Foglalás lemondása -|-" + szin.Zaras +"   "  + szin.Alahuzas + szin.Kek +  "-|- 3) foglalások listázása -|-" + szin.Zaras)
    print("Üsse be a használni kívánt funkció számát: ")
    bemenetFeldolgozas()

def jegyFoglalasKepernyo():
    pass

def lemondasKepernyo():
    pass

def listazasKepernyo():
    print(r"                  / \ " + "                     PILLANATNYI FOGLALÁSOK LISTÁJA" )
    print(r"                 |^^|" + "")
    print(r"                 |{}|" + "")
    print(r"  _______________/~~\________________" + "")
    print(r" /               |  |                \ " + "")
    print(r"`========--------.  .---------========'" + "")
    print(r"                 ||||" + "")
    print(r"                  ||" + "")
    print(r"                  ||" + "")
    print(r"                  ||" + "")
    print(r"                  ||" + "")
    print(r"              ,---||---," + "")
    print(r"              '---<>---'" + "")
    print(r"Üssön 0-t (nulla) a kezdőképernyőhöz történő visszatéréshez")
    bemenetFeldolgozas()