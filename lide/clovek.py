# Trida clovek - trida - predpis podle ktereho se vytvari objekty
from abc import ABC, abstractmethod


class Clovek(ABC):

    # Konstruktor - metoda ktera se vola ve chvili vytvareni
    # objektu
    def __init__(self, jmeno, vek):
        self._jmeno = jmeno
        self._vek = vek  # vek s podtrzitkem ( _ ) je privatni
        # (jakoby)

    # @abstractmethod
    def vrat_povolani(self):
        pass

    @property
    def jmeno(self):
        return self._jmeno

    @jmeno.getter
    def jmeno(self):
        print("druhy getter")
        return self._jmeno

    @property
    def vek(self):
        return self._vek

    @vek.setter
    def vek(self,novy_vek):
        if novy_vek >= 0:
            self._vek = novy_vek
        else:
            print("Nelze nastavit zaporny vek")

    # def set_vek(self, novy_vek):
    #     if novy_vek >=0:
    #         self._vek = novy_vek
    #     else:
    #         print("Nelze nastavit zaporny vek")

    # Metoda (funkce) pozdrav - neco co clovek dela
    # Ma nepovinny parametr pozdrav
    def vrat_pozdrav(self, pozdrav="CAU"):
        return f"{pozdrav} jsem {self._jmeno},\n mam {self._vek}"

    def __str__(self):
        return "Jsem clovek"
