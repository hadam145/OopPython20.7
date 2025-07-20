from zvire import Zvire


class Kocka(Zvire):

    def __init__(self, vaha, barva, hracka="pericko"):
        super().__init__(vaha,barva)
        self._hracka = hracka

    @property
    def hracka(self):
        return self._hracka

    def vrat_zvuk(self):
        return "Mnauuuuu mnauuuuu"