from clovek import Clovek

#Trida programator dedi z tridy clovek - Kulate zavorky ()
class Programator(Clovek):

#Konstruktor tridy programatora - pridava navic jazyk
    def __init__(self, jmeno, vek, jazyk):
        #Zde vola konstruktor predka (Clovek)
        super().__init__(jmeno, vek)
        self._jazyk = jazyk

#Metoda pro vraceni pozdravu
    def vrat_pozdrav(self, pozdrav="HELLO WORLD"):
        #Vola se tu pomoci `super()` metoda `vrat_pozdrav()` z predka
        #a pridava se navic neco noveho
        return super().vrat_pozdrav(pozdrav) + f"programuju v {self._jazyk}"

    #Magicka metoda - prevod instance na text
    def __str__(self):
        return super().__str__() + " ale programuji"

#Vytvoreni instance tridy `Programator`
tomas = Programator("Tomas", 25, "C#")

petr = Clovek("Petr",10)
print(petr)
print(tomas)

# print(tomas.jmeno)
#
# print(tomas.vrat_pozdrav("AHOJ"))
#
# cisla = [0,4,5,6]
#
# #Pole lidi (Programator a Clovek)
# lide = [
#     tomas,
#     Clovek("Marek",15)
# ]
# print("----------------")
# for clovek in lide:
#     #Vyuzivame polymorfismu
#     print(clovek.vrat_pozdrav())
#

