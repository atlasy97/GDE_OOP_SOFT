# AUTHOR: ATTILA PARAIZS
# NEPTUN CODE: XT121U
# 2024

from Funkciok.Funkciok import *
from Funkciok.Kepernyok import *
from Funkciok.Validaciok import *
from Osztalyok.BelfoldiJarat import BelfoldiJarat
from Osztalyok.LegiTarsasag import Legitarsasag
from Osztalyok.NemzetkoziJarat import NemzetkoziJarat

kezdoKepernyo()
Legitarsasag(1,"WizzAir", "ABCD123")
BelfoldiJarat(1,"Debrecen",12000)
NemzetkoziJarat(1,"Dubai",150000)
NemzetkoziJarat(2, "Barcelona", 45000)

while True:
    bemenetFeldolgozas()


