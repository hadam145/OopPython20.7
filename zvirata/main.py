from pes import Pes
from kachna import Kachna
from kocka import Kocka
from zvire import Zvire

zvire = Zvire(5)

kocka = Kocka(10,"Ruzova")

kachna = Kachna(2,"Zluta",True)
pes = Pes(20,"Zeleny",False)

zvirata = [
    kachna,
    zvire,
    pes,
    kocka
]

for zvire in zvirata:
    print(zvire.vrat_zvuk())

for zvire in zvirata:
    print(zvire)





